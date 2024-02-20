function generateHashtag(str) {
  if (str === "") {
    return false;
  }

  let words = str.toLowerCase();

  return "#" + words;
}

print(generateHashtag("codewars"));
