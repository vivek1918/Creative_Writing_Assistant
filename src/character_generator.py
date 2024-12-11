import random

class CharacterGenerator:
    def __init__(self):
        self.templates = {
            "romance": [
                {
                    "archetype": "The Passionate Dreamer",
                    "description": "A hopeless romantic who believes in true love",
                    "background_details": [
                        "Comes from a small town with big dreams",
                        "Has been hurt in past relationships",
                        "Works in a creative profession"
                    ],
                    "personality_traits": [
                        "Emotional and deeply empathetic",
                        "Believes in grand romantic gestures",
                        "Struggles with vulnerability"
                    ]
                },
                {
                    "archetype": "The Guarded Professional",
                    "description": "A successful career-focused individual who has closed off their heart",
                    "background_details": [
                        "Dedicated to career advancement",
                        "Has trust issues from past heartbreaks",
                        "Secretly longs for deep connection"
                    ],
                    "personality_traits": [
                        "Ambitious and driven",
                        "Appears confident but emotionally reserved",
                        "Values independence above all"
                    ]
                }
            ],
            "sci-fi": [
                {
                    "archetype": "The Reluctant Hero",
                    "description": "An ordinary individual thrust into extraordinary circumstances",
                    "background_details": [
                        "Grew up on a desolate space colony",
                        "Possesses unique skills unbeknownst to them",
                        "Fascinated by advanced technology"
                    ],
                    "personality_traits": [
                        "Cautious but resourceful",
                        "Driven by a strong moral compass",
                        "Harbors deep curiosity about the unknown"
                    ]
                },
                {
                    "archetype": "The Visionary Scientist",
                    "description": "A genius who sees possibilities others cannot",
                    "background_details": [
                        "Once worked for a corrupt organization",
                        "Driven to push the boundaries of human knowledge",
                        "Seeks redemption for past mistakes"
                    ],
                    "personality_traits": [
                        "Obsessive and focused",
                        "Socially awkward but kind-hearted",
                        "Unwavering belief in the power of science"
                    ]
                }
            ],
            "mystery": [
                {
                    "archetype": "The Intrepid Investigator",
                    "description": "A detective who stops at nothing to uncover the truth",
                    "background_details": [
                        "Lost a loved one to an unsolved crime",
                        "Works tirelessly to solve cold cases",
                        "Has a network of secret informants"
                    ],
                    "personality_traits": [
                        "Perceptive and detail-oriented",
                        "Determined but sometimes reckless",
                        "Has a dry sense of humor"
                    ]
                },
                {
                    "archetype": "The Enigmatic Stranger",
                    "description": "A mysterious figure with a hidden agenda",
                    "background_details": [
                        "Operates in the shadows",
                        "Has a troubled and secretive past",
                        "Possesses uncanny insight into human behavior"
                    ],
                    "personality_traits": [
                        "Calm under pressure",
                        "Highly analytical",
                        "Reluctant to form close relationships"
                    ]
                }
            ],
            "fantasy": [
                {
                    "archetype": "The Chosen One",
                    "description": "A destined hero foretold in ancient prophecies",
                    "background_details": [
                        "Grew up unaware of their lineage",
                        "Bears a mysterious mark or artifact",
                        "Longs for a life of adventure"
                    ],
                    "personality_traits": [
                        "Courageous but naive",
                        "Loyal to friends and allies",
                        "Determined to prove themselves"
                    ]
                },
                {
                    "archetype": "The Cunning Sorcerer",
                    "description": "A master of magic with a thirst for knowledge",
                    "background_details": [
                        "Trained in an ancient and secretive order",
                        "Seeks to uncover forbidden spells",
                        "Once betrayed by a trusted ally"
                    ],
                    "personality_traits": [
                        "Brilliant and calculating",
                        "Proud but protective",
                        "Driven by an insatiable curiosity"
                    ]
                }
            ]
        }

    def generate_character(self, genre="romance", traits=None):
        if genre not in self.templates:
            raise ValueError(f"Genre '{genre}' is not supported.")

        # Select a random template based on the chosen genre
        template = random.choice(self.templates[genre])

        # Generate a name
        first_names = ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Ethan', 'Sophia', 'Mason']
        last_names = ['Roberts', 'Thompson', 'Anderson', 'Martinez', 'Chen', 'Sullivan', 'Kim', 'Patel']
        name = f"{random.choice(first_names)} {random.choice(last_names)}"

        # Incorporate additional traits if provided
        additional_traits = traits if traits else []
        all_traits = template['personality_traits'] + additional_traits

        # Create character profile
        character_profile = f"""Character Profile: {genre.capitalize()} Genre

Name: {name}
Archetype: {template['archetype']}
Description: {template['description']}

Background:
{chr(10).join('- ' + detail for detail in template['background_details'])}

Personality Traits:
{chr(10).join('- ' + trait for trait in all_traits)}

Potential Challenges:
- Overcoming personal limitations
- Facing conflicts unique to their journey
- Discovering their true potential

Character Arc:
From {template['background_details'][1]} to a transformative journey of growth and self-discovery.
"""
        return character_profile


# Example Usage
generator = CharacterGenerator()
print(generator.generate_character(genre="sci-fi", traits=["Quick thinker", "Loves exploring new worlds"]))
