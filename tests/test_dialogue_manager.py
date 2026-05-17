import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from screening_ai.conversation_engine import ConversationStateMachine

def test_flow():
    print("🧪 Running Test: Graph-Based State Machine...")
    flow = {
        "start": "Q1",
        "nodes": {
            "Q1": {"question": "Test Question", "next": "END"}
        }
    }
    engine = ConversationStateMachine(flow)
    
    assert engine.get_question() == "Test Question"
    engine.next()
    assert engine.is_end() == True
    print("✅ Test Passed! Node traversal works perfectly.")

if __name__ == "__main__":
    test_flow()