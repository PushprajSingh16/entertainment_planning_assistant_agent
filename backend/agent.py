from llm import run_llm

class PlannerAgent:

    def run(self, movie: str, city: str):

        prompt = f"""
User wants to plan entertainment.

Movie / Event: {movie}
City: {city}

Provide a comprehensive plan including:
• Popular theatres (realistic names)
• Common show timings
• Expected ticket price range (INR)
• Public opinion and ratings
• Nearby attractions and activities
• Best transportation options
• Recommended restaurants nearby
• Weather considerations
• Accommodation suggestions if applicable
• Safety tips
• Final recommendation (3–4 lines)

Respond clearly in bullet points with sections.
"""

        output = run_llm(prompt)

        return {
            "movie": movie,
            "city": city,
            "plan": output
        }