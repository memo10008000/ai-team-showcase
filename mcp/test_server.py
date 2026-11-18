"""Unit & Integration verification for ai-team-mcp tools."""

import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from server import (
    list_personas,
    summon_persona,
    get_project_status,
    query_knowledge_base,
    get_governance_rule,
)


def run_tests():
    print("=" * 60)
    print("🧪 Testing ai-team-mcp Tools")
    print("=" * 60)

    # 1. Test list_personas
    print("\n[Test 1] Testing list_personas()...")
    roster = list_personas()
    assert "Elena Vasquez" in roster or "01" in roster, "Elena Vasquez should be in roster"
    assert "Adrian Torres" in roster or "07" in roster, "Adrian Torres should be in roster"
    print("  ✅ list_personas() passed! Found expected personas in roster.")

    # 2. Test summon_persona by ID
    print("\n[Test 2] Testing summon_persona('07')...")
    adrian = summon_persona("07")
    assert "Adrian Torres" in adrian or "enterprise_tech_architect" in adrian, "Failed to summon Adrian Torres"
    print("  ✅ summon_persona('07') passed!")

    # 3. Test summon_persona by alias
    print("\n[Test 3] Testing summon_persona('@Tech')...")
    adrian_alias = summon_persona("@Tech")
    assert "Adrian" in adrian_alias or "Enterprise Tech Architect" in adrian_alias or "07" in adrian_alias, "Failed to summon via @Tech"
    print("  ✅ summon_persona('@Tech') passed!")

    # 4. Test get_project_status
    print("\n[Test 4] Testing get_project_status()...")
    status = get_project_status("dashboard")
    assert "PROJECT_TRACKER" in status or "Executive Dashboard" in status or "Active Sprints" in status, "Tracker status failed"
    print("  ✅ get_project_status('dashboard') passed!")

    # 5. Test query_knowledge_base
    print("\n[Test 5] Testing query_knowledge_base('architecture')...")
    kb_res = query_knowledge_base("architecture")
    assert "architecture" in kb_res.lower() or "knowledge base" in kb_res.lower(), "KB query failed"
    print("  ✅ query_knowledge_base('architecture') passed!")

    # 6. Test get_governance_rule
    print("\n[Test 6] Testing get_governance_rule('Rule 30')...")
    rule = get_governance_rule("Rule 30")
    assert "Rule 30" in rule or "Permissions" in rule or "AI_GOVERNANCE" in rule, "Rule 30 lookup failed"
    print("  ✅ get_governance_rule('Rule 30') passed!")

    print("\n" + "=" * 60)
    print("🎉 ALL 6 MCP TOOL TESTS PASSED SUCCESSFULLY!")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
