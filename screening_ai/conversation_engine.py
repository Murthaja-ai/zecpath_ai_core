import json
import os

class ConversationStateMachine:
    def __init__(self, flow):
        self.flow = flow["nodes"]
        self.current_node = flow["start"]
        self.retry_count = {}

    def get_question(self):
        return self.flow[self.current_node]["question"]

    def next(self):
        self.current_node = self.flow[self.current_node].get("next", "END")

    def handle_silence(self):
        node = self.flow[self.current_node]
        retry_node = node.get("on_silence")
        
        if retry_node:
            self.retry_count.setdefault(self.current_node, 0)
            self.retry_count[self.current_node] += 1
            
            if self.retry_count[self.current_node] <= node.get("max_retries", 2):
                self.current_node = retry_node
            else:
                self.current_node = "END"
        else:
            self.next() # If no silence logic exists, just move on

    def handle_confusion(self):
        node = self.flow[self.current_node]
        if "on_confusion" in node:
            self.current_node = node["on_confusion"]
        else:
            self.next()

    def handle_repeat(self):
        node = self.flow[self.current_node]
        if "on_repeat" in node:
            self.current_node = node["on_repeat"]
        else:
            self.next()

    def is_end(self):
        return self.current_node == "END"

# --- Quick Test ---
if __name__ == "__main__":
    from error_handling import detect_issue
    
    # Load the JSON blueprint
    base_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base_dir, "conversation_flow.json"), "r") as f:
        flow = json.load(f)
            
    engine = ConversationStateMachine(flow)
    
    print("\n--- LIVE INTERVIEW SIMULATION ---")
    print("(Type your answers below. To simulate silence, just press ENTER without typing.)")
    print("-" * 50)
    
    while not engine.is_end():
        print(f"\n🤖 AI: {engine.get_question()}")
        
        # Let the user actually type the answer!
        answer = input("👤 You: ")
        
        issue = detect_issue(answer)
        print(f"   -> [System detected: {issue}]")
        
        if issue == "silence":
            engine.handle_silence()
        elif issue == "confusion":
            engine.handle_confusion()
        elif issue == "repeat":
            engine.handle_repeat()
        else:
            engine.next()
            
    print("\n✅ AI: That covers all my questions. Interview Complete!")