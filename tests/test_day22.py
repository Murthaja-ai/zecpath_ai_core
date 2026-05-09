import os
import json

def test_question_bank():
    # 1. Find the file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, "data", "demo_dataset", "screening_questions.json")
    
    print("🚀 Booting up Day 22 Question Bank Test...")
    
    # 2. Try to load the file
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            dataset = json.load(file)
            
            # 3. Print a success report
            version = dataset["metadata"]["version"]
            categories = list(dataset["question_bank"].keys())
            
            print(f"✅ Successfully loaded Question Bank Version: {version}")
            print(f"✅ Found {len(categories)} conversation categories: {', '.join(categories)}")
            
            # 4. THE FIX: Handle the Multilingual Dictionary
            # Grab the whole question object first
            sample_question_object = dataset["question_bank"]["Skills"][0]
            
            # Look inside the "text" dictionary and specifically grab the English string
            english_text = sample_question_object["text"]["en"]
            
            # NOW we can safely format the string
            injected_question = english_text.format(missing_skill="Data Visualization")
            
            print("\n🤖 AI Dynamic Question Test (English):")
            print(f"-> {injected_question}")
            
    except Exception as e:
        print(f"❌ Error loading JSON: {e}")

if __name__ == "__main__":
    test_question_bank()