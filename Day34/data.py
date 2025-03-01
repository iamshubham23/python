import requests
parameter={
    "amount":10,
    "type":"boolean"
}
response=requests.get("https://opentdb.com/api.php",params=parameter)
response.raise_for_status()
data=response.json()
question_data=print(data["results"])
question_data=[
   {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Film",
      "question": "Samuel L. Jackson had the words, &#039;Bad Motherf*cker&#039; in-scripted on his lightsaber during the filming of Star Wars.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Film",
      "question": "The word &quot;Inception&quot; came from the 2010 blockbuster hit &quot;Inception&quot;.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Film",
      "question": "In Alfred Hitchcock&#039;s film &#039;Psycho&#039; it is said he used chocolate syrup to simulate the blood in the famous shower scene from ",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Film",
      "question": "Ewan McGregor did not know the name of the second prequel film of Star Wars during and after filming.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Film",
      "question": "In the original Star Wars trilogy, David Prowse was the actor who physically portrayed Darth Vader.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Film",
      "question": "The movie &quot;The Nightmare before Christmas&quot; was all done with physical objects.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Film",
      "question": "Matt Damon played an astronaut stranded on an extraterrestrial planet in both of the movies Interstellar and The Martian.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Film",
      "question": "&quot;Minions&quot; was released on the June 10th, 2015.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Film",
      "question": "Han Solo&#039;s co-pilot and best friend, &quot;Chewbacca&quot;, is an Ewok.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Entertainment: Film",
      "question": "George Lucas directed the entire original Star Wars trilogy.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    }
  ]
