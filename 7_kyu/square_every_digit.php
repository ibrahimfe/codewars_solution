function square_digits($num): int {
  $str = strval($num);
  $arr = str_split($str);
  $result = "";
  for ($i = 0; $i < strlen($str); $i++) {
    $arr[$i] = intval($arr[$i] * $arr[$i]);
    $result = $result . strval($arr[$i]);
  }
  return intval($result);
}