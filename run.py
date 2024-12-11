import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.main import CreativeWritingAssistant

def main():
    assistant = CreativeWritingAssistant()
    
    print("=== Creative Writing Assistant ===")
    
    while True:
        print("\nChoose an option:")
        print("1. Generate Character")
        print("2. Generate Plot")
        print("3. Generate Dialogue")
        print("4. Style Transfer")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            genre = input("Enter genre (optional): ")
            traits = input("Enter character traits (comma-separated, optional): ").split(',')
            character = assistant.generate_character(genre, traits)
            print("\nGenerated Character:\n", character)
        
        elif choice == '2':
            genre = input("Enter genre: ")
            complexity = input("Enter complexity (low/medium/high): ")
            plot = assistant.generate_plot(genre, complexity)
            print("\nGenerated Plot:\n", plot)
        
        elif choice == '3':
            characters = input("Enter character names (comma-separated): ").split(',')
            context = input("Enter dialogue context: ")
            dialogue = assistant.generate_dialogue(characters, context)
            print("\nGenerated Dialogue:\n", dialogue)
        
        elif choice == '4':
            text = input("Enter text to transform: ")
            target_style = input("Enter target style: ")
            styled_text = assistant.transfer_style(text, target_style)
            print("\nStyled Text:\n", styled_text)
        
        elif choice == '5':
            print("Thank you for using Creative Writing Assistant!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()