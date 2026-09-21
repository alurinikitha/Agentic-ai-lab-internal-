from openai import OpenAI

client = OpenAI()

# Read the original text
with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Step 1
step1 = client.responses.create(
    model="gpt-5.6-luna",
    input=f"""
Extract the important information from this text.

Identify:
1. Main topic
2. Key points
3. Benefits
4. Challenges
5. Conclusion

Do not summarize yet.

Text:
{text}
"""
)

output1 = step1.output_text

# Step 2
step2 = client.responses.create(
    model="gpt-5.6-luna",
    input=f"""
Organize the following information into logical sections.
Remove duplicate information.
Do not add new information.

Information:
{output1}
"""
)

output2 = step2.output_text

# Step 3
step3 = client.responses.create(
    model="gpt-5.6-luna",
    input=f"""
Write an 80-100 word summary using the information below.
Use simple English and keep the original meaning.

Information:
{output2}
"""
)

output3 = step3.output_text

# Step 4
step4 = client.responses.create(
    model="gpt-5.6-luna",
    input=f"""
Review the summary below for:
- Accuracy
- Missing information
- Repetition
- Grammar
- Clarity

Return only the improved final summary.

Information:
{output2}

Summary:
{output3}
"""
)

final_summary = step4.output_text

print("\nFINAL SUMMARY:\n")
print(final_summary)