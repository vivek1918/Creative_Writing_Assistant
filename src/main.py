import os
from dotenv import load_dotenv
from .style_transfer import StyleTransfer
from .character_generator import CharacterGenerator
from .plot_generator import PlotGenerator
from .dialogue_generator import DialogueGenerator

class CreativeWritingAssistant:
    def __init__(self):
        load_dotenv()
        self.style_transfer = StyleTransfer()
        self.character_generator = CharacterGenerator()
        self.plot_generator = PlotGenerator()
        self.dialogue_generator = DialogueGenerator()

    def generate_character(self, genre=None, traits=None):
        """Generate a detailed character profile."""
        return self.character_generator.generate_character(genre, traits)

    def generate_plot(self, genre, complexity='medium'):
        """Generate a plot for a given genre."""
        return self.plot_generator.generate_plot(genre, complexity)

    def generate_dialogue(self, characters, context):
        """Generate dialogue between characters."""
        return self.dialogue_generator.generate_dialogue(characters, context)

    def transfer_style(self, text, target_style):
        """Transfer writing style of a given text."""
        return self.style_transfer.transfer_style(text, target_style)

def main():
    assistant = CreativeWritingAssistant()
    
    # Example usage demonstrations
    print("Character Generation:")
    character = assistant.generate_character(genre='fantasy', 
                                             traits=['brave', 'mysterious'])
    print(character)

    print("\nPlot Generation:")
    plot = assistant.generate_plot(genre='sci-fi', complexity='high')
    print(plot)

if __name__ == "__main__":
    main()