
// forEachのテスト
function f2_1(){
    var data = [3, 7, 9, 2, 1, 11];
    var sum = 0;
    data.forEach(function(d){
        sum += d;
    });
    console.log("sum:" + sum);
}

// underscore.js入門
function f2_3(){
    // underscore test

    // A
    journeys = [
        {period: "morning", times:[44, 34, 56, 31]},
        {period: "evening", times:[35, 33]},
        {period: "morning", times:[33, 29, 35, 41]},
        {period: "evening", times:[24, 45, 27]},
        {period: "evening", times:[18, 23, 28]}
    ];

    var groups = _.groupBy(journeys, "period");

    console.log("groups: " + groups);

    // pluck: phpのarray_columns
    var mTimes = _.pluck(groups['morning'], 'times');

    mTimes = _.flatten(mTimes);
    console.log(mTimes);
    var average = function(l){
        var sum = _.reduce(l, function(a, b){ return a + b }, 0);
        return sum / l.length;
    }
    console.log('Average morning time is ' + average(mTimes));

    // B

    var nums = [];
    for(var i = 1; i <= 10; i++){
        nums.push(i);
    }
    console.log(nums);

    // filter: falseが返された要素を削除した配列を返す
    var filtered = nums.filter(function(o){ return o % 2});
    console.log("filtered: " + filtered);
    var square = filtered.map(function(o){return o * o;});
    console.log("square: " + square);
    var reduce = square.reduce(function(a, b){return a + b;});
    console.log("reduced: " + reduce);
}


function f2_4_clojure(){

    function Counter(inc){
        var count = 0;
        var add = function(){
            count += inc;
            console.log("current count: " + count);
        }
        return add;
    }

    var inc2 = Counter(2);
    inc2();
    inc2();
}

function f2_5_clojure_api(){

    function Counter(inc){
        var count = 0;
        var api = {};

        api.add = function(){
            count += inc;
            console.log('[add] Current count: ' + count);
        }

        api.sub = function(){
            count -= inc;
            console.log('[sub] Current count: ' + count);
        }

        api.reset = function(){
            count = 0;
            console.log("[reset] Count reset to 0");
        }

        return api;
    }

    var cntr = Counter(3);
    cntr.add();
    cntr.add();
    cntr.sub();
    cntr.reset();
    cntr.add();
}

// f2_3();
// f2_4_clojure();
f2_5_clojure_api();








