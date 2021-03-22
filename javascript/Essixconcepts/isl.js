

//team name

isl_2020.map(object=>object.team).forEach(team=>console.log(team))



//sort the teams order of their matches played

isl_2020.sort((obj1,obj2)=>obj1.mp>obj2.mp?1:-1).forEach(obj=>console.log(obj))



//hihest point team


const mpt=isl_2020.map(obj=>obj.pts).reduce((pt1,pt2)=>pt1>pt2?pt1:pt2)
console.log(mpt);

let res=isl_2020.sort((obj1,obj2)=>obj1.pts>obj2.pts?-1:1)[0]
console.log(res);
