students = ["ALALLAAPAA","ALLLAAAPAA","APAPALLAAA"]

//결석3번 0점, 10점시작, 출석+1점, 지각 2번->결석1번으로 처리, 결석1번 -1점
//학생번호 1,2,3
//점수가 높은 순으로 내림차순
//score=[점수,지각,결석]
function scoring(char, score){

    if(char==='A'){
        score[0] = score[0]+1
    }else if(char==='L'){
        if(score[1]===2){
            score[0] = score[0]-1
            score[1] = 0
            score[2] += 1
        }else{
            score[1] = score[1] + 1
        }
    }else if(char==='P'){
        score[2]+=1
        score[0]-=1
    }

    return score
}

function solution(students){
    res = []

    scores = Array.from({length:students.length}, () => 0)

    s = students.map((student, idx)=>{
        score = [10,0,0]
        for(let i=0;i<student.length;i++){
            score = scoring(student[i], score)
            if(score[2]===3) return [0, idx]
        }
        return [score[0], idx]
    })

    res = s.sort((a,b)=>{
        if((a[0]-b[0])===0){

        }
        return b[0]-a[0]
    })

    res = s.map((item)=>{
        return item[1]+1
    })

    return res
}

console.log(solution(students))