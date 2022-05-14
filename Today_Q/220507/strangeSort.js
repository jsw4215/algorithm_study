numbers = [3,5,4,1,6]

function solution(numbers){
    res = []

    temp = numbers.sort((a,b)=> b-a)

    let checker = true
    while (temp.length!==0){     
        let num = 0
        if (checker){
           num = temp.shift()
           checker = false
        }else{
           num = temp.pop()
           checker = true
        }

        res.push(num)
         
    }

    return res
}  

console.log(solution(numbers))