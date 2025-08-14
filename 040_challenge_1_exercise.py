# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging than the example.

# Write a function that takes a list of words and returns a report of all the
# words that are longer than 10 characters but don't contain a hyphen. If those
# words are longer than 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  words_longer_than_10_chars = get_words_longer_than_10_chars(words)
  hyphens_removed = remove_words_with_hyphens(words_longer_than_10_chars)
  with_ellipsis = add_ellipsis(hyphens_removed)

  return "These words are quite long: " + ", ".join(with_ellipsis)

def get_words_longer_than_10_chars(words):
  words_longer_than_10_chars = []

  for word in words:
    if len(word) > 10:
      words_longer_than_10_chars.append(word)
  
  return words_longer_than_10_chars

def remove_words_with_hyphens(words):
  words_without_hyphens = []

  for word in words:
    if "-" not in word:
      words_without_hyphens.append(word)
  
  return words_without_hyphens

def add_ellipsis(words):
  with_ellipsis = []

  for word in words:
    if len(word) > 15:
      with_ellipsis.append(word[:15] + "...")
    else:
      with_ellipsis.append(word)

  return with_ellipsis





check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
