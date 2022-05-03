function solution(bakery_schedule, current_time, K){

    const curr_h_m = current_time.split(":")
    let ans = 0
    let time_diff = -1

    for(let i=0;i<bakery_schedule.length;i++){
        
        const time_and_bread = bakery_schedule[i].split(" ")
        const hour_and_minutes = time_and_bread[0].split(":")

        if (Number(hour_and_minutes[0]) > Number(curr_h_m[0])){
            ans+=Number(time_and_bread[1])

            if(ans >= K){
                time_diff = (Number(hour_and_minutes[0]) - Number(curr_h_m[0]))*60 + (Number(hour_and_minutes[1]) - Number(curr_h_m[1]))
                
                return time_diff

            }

            
        }else if(Number(hour_and_minutes[0]) == Number(curr_h_m[0])){
            if(Number(hour_and_minutes[1]) >= Number(curr_h_m[1])){
                ans+=Number(time_and_bread[1])

                if(ans >= K){
                    time_diff = (Number(hour_and_minutes[0]) - Number(curr_h_m[0]))*60 + (Number(hour_and_minutes[1]) - Number(curr_h_m[1]))
                
                    return time_diff
                }

                
            }
        }
        
    }

    return time_diff

}

console.log(solution(["09:05 10", "12:20 5","13:25 6","14:24 5"],"12:05",10))