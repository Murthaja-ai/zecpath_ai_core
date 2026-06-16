# optimization_core/intent_parser.py

class NLPIntentRefiner:
    @staticmethod
    def classify_intent(text: str) -> str:
        """
        Optimizes Natural Language Processing (NLP) intent detection.
        Upgrades slow list-scanning to high-speed Set intersections.
        """
        # Clean and tokenize the text
        text_lower = text.lower()
        words = set(text_lower.replace(",", "").replace(".", "").split())
        
        # Categorized Intent Sets (O(1) lookup time)
        experience_keywords = {"built", "developed", "implemented", "created", "led"}
        education_keywords = {"learned", "studied", "course", "degree", "graduated"}
        future_keywords = {"will", "plan", "future", "goal", "aim"}
        
        # Fast mathematical set intersection
        if words.intersection(experience_keywords):
            return "experience"
        if words.intersection(education_keywords):
            return "education"
        if words.intersection(future_keywords):
            return "future_intent"
            
        return "generic"