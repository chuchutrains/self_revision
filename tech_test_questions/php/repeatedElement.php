<?php

$arrSize = 3;
$arrStr = "1 5 1";
$arr = explode(" ", $arrStr);

$arrUniSize = count(array_unique($arr));
if ($arrSize != $arrUniSize) echo "happy";
else echo "sad";
?>