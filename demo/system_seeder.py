# demo_data/system_seeder.py
import json
import asyncio
import hashlib
import re
from statistics import stdev

# --- MOCKING ENTERPRISE IMPORTS FOR DEMO PURPOSES ---
def mask_pii(text: str) -> str:
    text = re.sub(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', '[MASKED_EMAIL]', text)
    return re.sub(r'\+?\d{1,3}?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', '[MASKED_PHONE]', text)

def generate_hash(data: dict, prev_hash: str) -> str:
    record = json.dumps(data, sort_keys=True).encode('utf-8')
    return hashlib.sha256(record + prev_hash.encode('utf-8')).hexdigest()

# --- THE SIMULATION ENGINE ---
async def process_candidate(candidate: dict, prev_hash: str) -> dict:
    print(f"\n[GATEWAY] Receiving Payload for {candidate['candidate_id']}...")
    
    # 1. Privacy Filter (Day 61)
    safe_email = mask_pii(candidate['personal_data']['email'])
    print(f"  ↳ [TELEMETRY] PII Masked: {safe_email}")

    # 2. Hard Gate Integrity Check (Day 52)
    flags = candidate['security_flags']
    if flags['tab_switch_count'] > 5 or flags['off_screen_focus']:
        print(f"  ↳ 🚨 [SECURITY] Malpractice Detected! Zeroing scores.")
        final_score = 0
        decision = "Rejected (Integrity Violation)"
    else:
        # 3. Dynamic Variance Math (Day 54)
        scores = list(candidate['raw_scores'].values())
        avg = sum(scores) / len(scores)
        variance_penalty = stdev(scores) * 0.4 if len(scores) > 1 else 0
        final_score = round(max(0, avg - variance_penalty), 2)
        
        if final_score >= 80: decision = "Selected"
        elif final_score >= 60: decision = "Hold / Human Review"
        else: decision = "Rejected"
        
        print(f"  ↳ [AI MATH] Avg: {avg:.1f} | Variance Penalty: -{variance_penalty:.1f} | Final: {final_score}")

    # 4. Cryptographic Vault (Day 61)
    audit_record = {"id": candidate['candidate_id'], "score": final_score, "decision": decision}
    crypto_hash = generate_hash(audit_record, prev_hash)
    print(f"  ↳ 🔒 [VAULT] Decision Locked. Hash: {crypto_hash[:16]}...")
    
    return crypto_hash

async def run_live_demo():
    print("🚀 INITIALIZING ZECPATH ENTERPRISE DEMO SEEDER")
    print("="*50)
    
    with open('demo/dataset.json', 'r') as f:
        data = json.load(f)
        
    current_hash = "GENESIS_BLOCK_0000"
    
    # Simulating Day 60 Concurrent Processing
    for candidate in data['candidates']:
        current_hash = await process_candidate(candidate, current_hash)
        await asyncio.sleep(0.5) # Slight pause for visual dramatic effect during demo

    print("\n✅ DEMO SEEDING COMPLETE. DASHBOARDS POPULATED.")

if __name__ == "__main__":
    asyncio.run(run_live_demo())