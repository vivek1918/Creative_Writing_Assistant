import json
import random
import os
from transformers import pipeline

class PlotGenerator:
    def __init__(self):
        # Get the absolute path to the project root
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        
        # Construct the full path to the genre prompts
        prompts_path = os.path.join(project_root, 'data', 'genre_prompts.json')
        
        # Load genre-specific plot structures
        try:
            with open(prompts_path, 'r') as f:
                self.genre_prompts = json.load(f)
        except FileNotFoundError:
            print(f"Warning: Genre prompts file not found at {prompts_path}")
            self.genre_prompts = {
                "default": {
                    "standard_plot": "A character embarks on an unexpected journey"
                }
            }
        
        # Initialize text generation pipeline
        self.generator = pipeline("text-generation", model="gpt2")

    def generate_plot(self, genre, complexity='medium'):
        complexity_map = {
            'low': 'simple_plot',
            'medium': 'standard_plot',
            'high': 'complex_plot'
        }
        plot_type = complexity_map.get(complexity, 'standard_plot')
        prompt_template = self.genre_prompts[genre].get(plot_type, "A routine space mission goes wrong.")
        
        # Add variations to the prompt
        prompt_variations = [
            f"Imagine a {complexity} sci-fi story: {prompt_template}",
            f"Write a {complexity} sci-fi plot outline: {prompt_template}",
            f"Describe a {complexity} plot for a sci-fi adventure: {prompt_template}",
            f"Generate a {complexity} science fiction story plot: {prompt_template}"
        ]
        full_prompt = random.choice(prompt_variations)

        # Generate plot
        plot_outline = self.generator(
            full_prompt, 
            max_length=150, 
            num_return_sequences=1, 
            do_sample=True,  # Enables non-deterministic outputs
            top_p=0.9,       # Nucleus sampling for varied results
            temperature=0.8  # Adds randomness
        )[0]['generated_text']
        
        return plot_outline

        