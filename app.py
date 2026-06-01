def generate_questions(role, experience):

  prompt = f""" 
  Generate 5 interview questions.

  target role {role}
  Experience level {experience}

  for each questions provide
  1.question
  2.difficuty
  3.sample answer
  4.what interviewers are looking for


  Include:
  - Promblem-solveing questions
  - Technical quesitions
  - Behavioral questions
  
  Format clearly.
  """

  response = client.models.generate_content(
      model="gemini-2.5-flash",
      contents=prompt
  )

  return response.text

role = input("Target role: ")
experience = input("experience level: ")

questions = generate_questions(role, experience)

print("\n--- Ai question generator ---\n")
print(questions)