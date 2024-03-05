function multiply(number) {
  const length = Math.abs(number).toString().length;
  return number * 5 ** length;
}
