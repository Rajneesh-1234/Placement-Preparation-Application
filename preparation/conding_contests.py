import streamlit as st

# =====================================================
# CODING CONTESTS & PRACTICE IDE
# =====================================================

def coding_contests_ui():

    st.title("🏆 Coding Contests & Practice IDE")
    st.caption(
        "Company-specific coding practice | No solutions | Write & test your own code"
    )

    st.divider()

    # =====================================================
    # PLATFORM SELECTION
    # =====================================================
    platform = st.selectbox(
        "Choose Coding Platform",
        [
            "HackerRank",
            "HackerEarth",
            "CodeChef",
            "LeetCode"
        ]
    )

    company = st.selectbox(
        "Choose Company",
        [
            "General Practice",
            "TCS",
            "Infosys",
            "Wipro",
            "Accenture",
            "Cognizant",
            "Capgemini",
            "SAP",
            "Amazon",
            "Microsoft",
            "Google"
        ]
    )

    st.divider()

    # =====================================================
    # QUESTIONS DATABASE (50+ QUESTIONS)
    # =====================================================
    questions = {
        "General Practice": [
            "Reverse an array",
            "Check if a number is palindrome",
            "Find the second largest element",
            "Rotate array by K positions",
            "Count frequency of characters in a string",
            "Find missing number in array",
            "Check balanced parentheses",
            "Remove duplicates from array",
            "Find GCD of two numbers",
            "Binary search implementation"
        ],

        "TCS": [
            "Find longest word in a sentence",
            "Replace characters in string",
            "Check automorphic number",
            "Convert decimal to binary",
            "Sort elements by frequency",
            "Count vowels and consonants",
            "Matrix addition",
            "Find first non-repeating character",
            "Check perfect square",
            "Remove special characters from string"
        ],

        "Infosys": [
            "Find equilibrium index of array",
            "Count pairs with given sum",
            "Check anagram strings",
            "Print Pascal triangle",
            "Find prime numbers in range",
            "Longest common prefix",
            "Rotate matrix 90 degrees",
            "Find leaders in array",
            "Check power of two",
            "Merge two sorted arrays"
        ],

        "Wipro": [
            "Find maximum subarray sum",
            "Check Armstrong number",
            "Reverse words in string",
            "Find duplicate elements",
            "Replace space with %20",
            "Check leap year",
            "Sort string characters",
            "Find sum of digits until single digit",
            "Check subset array",
            "Print pattern (star/number)"
        ],

        "Accenture": [
            "Find largest palindrome substring",
            "Count set bits",
            "Remove vowels from string",
            "Find missing characters in alphabet",
            "Check rotated string",
            "Calculate power without pow()",
            "Find majority element",
            "Find trailing zeros in factorial",
            "Check binary string",
            "Find smallest window substring"
        ],

        "Cognizant": [
            "Find common elements in arrays",
            "Count inversions",
            "Find minimum platforms required",
            "Check valid IP address",
            "Find peak element",
            "Find longest increasing subsequence",
            "Check happy number",
            "Find next greater element",
            "Find smallest positive missing number",
            "Spiral traversal of matrix"
        ],

        "Capgemini": [
            "Find sum of even numbers",
            "Check string rotation",
            "Find largest odd number in string",
            "Find Kth smallest element",
            "Check monotonic array",
            "Remove duplicates from string",
            "Check valid parentheses",
            "Find intersection of arrays",
            "Find minimum difference pair",
            "Count words in sentence"
        ],

        "SAP": [
            "Implement stack using array",
            "Implement queue using array",
            "Check redundant brackets",
            "Evaluate postfix expression",
            "Convert infix to postfix",
            "Find longest valid parentheses",
            "Detect cycle in linked list",
            "Reverse linked list",
            "Find middle of linked list",
            "Merge two linked lists"
        ],

        "Amazon": [
            "Two sum problem",
            "Longest substring without repeating characters",
            "Trapping rain water",
            "Container with most water",
            "LRU cache design",
            "Merge intervals",
            "Find kth largest element",
            "Valid sudoku",
            "Word ladder",
            "Binary tree level order traversal"
        ],

        "Microsoft": [
            "Longest common subsequence",
            "Edit distance",
            "Find cycle in directed graph",
            "Topological sort",
            "Detect bipartite graph",
            "Find bridges in graph",
            "Minimum spanning tree",
            "Word break problem",
            "Serialize and deserialize tree",
            "Find lowest common ancestor"
        ],

        "Google": [
            "Find shortest path in grid",
            "Alien dictionary",
            "Regular expression matching",
            "Median of two sorted arrays",
            "N-Queens problem",
            "Sudoku solver",
            "Trie implementation",
            "Find articulation points",
            "Knapsack problem",
            "String interleaving"
        ]
    }

    # =====================================================
    # DISPLAY QUESTIONS
    # =====================================================
    st.subheader(f"📌 {company} Coding Questions ({platform})")

    selected_questions = questions.get(company, [])

    question = st.selectbox(
        "Select a Coding Question",
        selected_questions
    )

    st.info(
        f"🧠 **Problem:** {question}\n\n"
        f"✍️ Write your own solution below. No solutions are provided."
    )

    # =====================================================
    # CODE EDITOR (IDE)
    # =====================================================
    st.subheader("💻 Coding IDE")

    language = st.selectbox(
        "Select Programming Language",
        ["Python", "Java", "C", "C++"]
    )

    starter_code = {
        "Python": "# Write your Python code here\n",
        "Java": "class Solution {\n    public static void main(String[] args) {\n        \n    }\n}\n",
        "C": "#include <stdio.h>\nint main() {\n    \n    return 0;\n}\n",
        "C++": "#include <bits/stdc++.h>\nusing namespace std;\nint main() {\n    \n    return 0;\n}\n"
    }

    code = st.text_area(
        "Code Editor",
        value=starter_code[language],
        height=300
    )

    st.warning(
        "⚠️ Code execution is disabled.\n"
        "This IDE is for **practice & interview preparation only**.\n"
        "Students are encouraged to test code on "
        f"{platform} platform."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.button("💾 Save Code (Local)")

    with col2:
        st.button("🧹 Clear Code")

    st.divider()

    st.success(
        "🚀 Practice consistently on HackerRank / CodeChef / LeetCode.\n"
        "Do NOT memorize solutions. Think, write, debug, and improve."
    )
