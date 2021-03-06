<?php

# 11th Feburary 2022 TOTO.
$quick_pick = 6;
$winning_numbers  = [9,13,14,16,18,28,10];
$myToto = [
    # 1st paper.
    [5,6,15,31,32,46],

    # 2nd paper.
    [3,15,19,31,32,48],
    [5,8,15,16,19,32],
    [12,13,27,40,44,47],
    
    # 3rd paper.
    [13,24,34,39,41,45],
    [6,12,22,23,33,39],
    [7,10,19,35,47,49],
    [8,16,26,30,42,48],
    [2,17,20,28,38,43],      
    [6,8,15,25,26,33],
    
    # 4th paper.
    [16,33,36,37,44,48],
    [6,9,16,28,34,41],
    [5,8,14,20,31,49],
    [4,20,22,37,39,45],
    [9,19,34,35,39,41],
    [2,19,29,31,34,38],

    # 5th paper.
    [12,25,29,31,35,43],
    [6,13,20,21,32,37],
    [6,11,22,28,36,39],
    [7,9,12,14,15,39],
    [2,7,13,22,28,33],
    [3,7,24,27,31,47],

    # 6th paper.
    [16,19,21,27,40,43],
    [7,25,41,42,43,47],
    [4,27,34,35,40,46],
    [12,19,28,29,32,37],
    [13,19,21,44,46,49],
    [1,21,22,26,28,31],

    # 7th paper.
    [4,12,16,18,24,30],
    [4,17,19,30,39,46],
    [18,25,27,30,43,44],
    [1,12,17,24,27,29],
    [5,21,22,24,29,34],
    [6,17,36,40,41,43],

    # 8th paper.
    [4,14,17,22,37,40],
    [5,7,9,10,14,29],
    [7,8,9,18,23,27],
    [3,8,18,22,29,30],
    [1,4,5,10,19,23],
    [2,5,6,8,24,44],

    # Charlotte's toto.
    # 9th paper.
    [6,13,20,32,41,44],
    [1,19,31,38,44,48],
    [2,22,34,40,48,49],
    [9,14,17,29,38,44],
    [5,8,13,24,33,48],
    [5,25,26,35,42,44],

    # 10th paper.
    [2,4,25,36,37,41],
    [5,8,11,15,24,30],
    [7,9,24,30,45,46],
    [2,6,11,28,38,49],
    [2,9,15,21,22,32],
    [5,11,17,21,25,46],

    # 11th paper.
    [10,16,19,29,30,43],
    [5,6,7,31,33,46],
    [7,11,26,41,46,47],
    [4,15,29,36,44,45],
    [16,18,32,39,42,44],
    [1,7,16,20,28,35],

    # 12th paper.
    [25,30,38,43,45,48],
    [1,3,8,15,16,42],
    [1,13,22,27,43,47],
    [5,6,32,39,40,42],
    [2,20,37,45,48,49],
    [10,12,24,26,28,35],

    # 13th paper.
    [1,2,3,13,30,33],
    [9,10,23,24,45,46],
    [18,22,24,28,36,49],
    [2,6,12,13,34,36],
    [4,10,14,27,34,42],
    [5,22,25,35,38,41],

    # 14th paper.
    [3,7,27,42,46,48],
    [16,18,21,28,31,34],
    [4,16,18,36,38,42],
    [9,14,33,34,36,39],
    [2,29,31,33,36,41],
    [2,3,7,12,20,40],

    # 15th paper.
    [3,21,23,33,39,42],
    [17,29,30,35,37,42],
    [2,8,23,32,40,47],
    [7,28,33,34,38,41],
    [2,3,18,34,45,49],
    [10,13,24,25,39,49],

    # 16th paper.
    [11,12,19,31,42,46],
    [8,23,24,41,46,47],
    [6,15,25,35,43,46],
    [2,12,20,22,39,49],
    [1,14,16,25,36,41],
    [17,21,24,26,27,49],

    # 17th paper.
    [3,14,25,29,36,47],
    [5,6,25,35,42,49],
    [11,17,20,21,26,47],
    [9,14,17,30,38,44],
    [1,21,31,32,36,49],
    [8,16,20,31,37,44],

    # 18th paper.
    [15,23,27,34,35,38],
    [8,29,31,32,34,44],
    [1,5,19,24,32,38],
    [15,23,25,29,32,46],
    [4,11,24,28,34,39],
    [15,23,26,32,44,47],

    # Cousins.
    // [17,21,25,34,35,39,46],
    // [6,8,12,14,18,27,42],
    // [22,23,24,26,29,33,46],
    // [6,12,14,22,23,25,39],
    // [10,13,16,19,21,31,32,35,41],

    # Simpson.
    [1,6,17,22,24,35],
];

$results =  [
    "0" => 0,
    "1" => 0,
    "2" => 0,
    "3" => 0,
    "4" => 0,
    "5" => 0,
    "6" => 0,
];
$count =  1;
foreach ($myToto as $row) {
    # Print my toto.
    $result = $count . ") [";
    $count++;
    foreach  ($row as $number) {
        $result .= $number . " ";
    }
    $result = substr($result, 0, -1);
    $result .= "] --> ";

    # Print match(s) result.
    $match = array_intersect($winning_numbers, $row);
    $result .= count($match) . " match(s)\n";
    echo $result;
    # Increment overall result count.
    $match_to_string = strval(count($match));
    $results[$match_to_string] += 1;
}

# Print overall result count.
echo "======================================================================\n";
foreach ($results as $match => $result) {
    echo $match . " match(s) : " . $result . "\n";
}
?>