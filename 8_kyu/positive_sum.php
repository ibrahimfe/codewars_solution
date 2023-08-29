function positive_sum($arr) {
  $sum = 0;
  for ($i = 0; $i < count($arr); $i++) {
    if ($arr[$i] > 0) {
      $sum += $arr[$i];
    }
  }
  return $sum;
}