from transformers import pipeline
import re

class StyleTransfer:
    def __init__(self):
        # Initialize text generation pipeline
        self.generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B', device=0)

    def transfer_style(self, text, target_style):
        """
        Transfer the style of a given text to a target style.
        """
        prompt = f"""Transform the following text into the style of {target_style}:

        Original: {text}

        Transformed:"""
        
        styled_text = self.generator(
            prompt, 
            max_length=100, 
            num_return_sequences=1
        )[0]['generated_text']
        
        # Post-process output to remove unwanted text
        styled_text = styled_text.split("Transformed:")[-1].strip()  # Extract main output
        styled_text = re.sub(r"[\*\_\-]+.*", "", styled_text)        # Remove markdown-like text
        return styled_text

if __name__ == "__main__":
    style_transfer = StyleTransfer()

    # Take user inputs
    original_text = input("Enter the text to transform: ")
    desired_style = input("Enter the target style (e.g., Shakespearean, Modern, Poetic): ")

    # Transform the text
    styled_text = style_transfer.transfer_style(original_text, desired_style)

    # Print the result
    print("\nStyled Text:")
    print(styled_text)