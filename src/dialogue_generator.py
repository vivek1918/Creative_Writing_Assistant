from transformers import pipeline

class DialogueGenerator:
    def __init__(self):
        # Initialize text generation pipeline
        self.generator = pipeline(
            'text-generation',
            model='EleutherAI/gpt-neo-1.3B',
            device=0
        )

    def generate_dialogue(self, characters, context):
        """
        Generate a clear dialogue between characters.

        :param characters: List of character names/descriptions
        :param context: Context or situation for the dialogue
        :return: Generated dialogue as a string
        """
        # Structured prompt enforcing dialogue format
        prompt = (
            f"Write a dialogue between {characters[0]} and {characters[1]} in this context: {context}.\n"
            f"Format the dialogue as follows:\n"
            f"{characters[0]}: [Line]\n"
            f"{characters[1]}: [Line]\n\nDialogue:\n"
        )

        dialogue = []
        current_prompt = prompt

        for _ in range(10):  # Limit the dialogue to 10 exchanges (5 per character)
            result = self.generator(
                current_prompt,
                max_length=150,
                num_return_sequences=1,
                temperature=0.7,
                top_k=50
            )[0]['generated_text']

            # Extract the dialogue continuation
            dialogue_start = result.find("Dialogue:")
            raw_dialogue = (
                result[dialogue_start + 9:].strip() if dialogue_start != -1 else result
            )

            # Clean and parse the line
            new_lines = self._clean_dialogue(raw_dialogue, characters).split("\n")
            if new_lines:
                new_line = new_lines[0]  # Take the first new line generated
                dialogue.append(new_line)
                current_prompt = prompt + "\n".join(dialogue)  # Update the prompt with the dialogue so far

                # Stop if the conversation seems to end naturally
                if new_line.lower().endswith(("?", ".", "!", "...")):
                    break

        return "\n".join(dialogue)

    def _clean_dialogue(self, dialogue, characters):
        """
        Post-process and clean up the generated dialogue.

        :param dialogue: Raw dialogue string
        :param characters: List of character names
        :return: Cleaned and structured dialogue
        """
        lines = dialogue.split("\n")
        cleaned_lines = []
        seen_lines = set()

        for line in lines:
            # Ensure line starts with a valid character name
            line = line.strip()
            if line and any(line.startswith(char + ":") for char in characters) and line not in seen_lines:
                cleaned_lines.append(line)
                seen_lines.add(line)

        return "\n".join(cleaned_lines)
