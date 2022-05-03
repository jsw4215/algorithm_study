function island_dfs_stack(grids){
    let grid = grids
    const dx = [0, 0, 1, -1]
    const dy = [1, -1, 0, 0]
    const rows = grid.length
    const cols = grid[0].length
    let cnt = 0
    let ans = []

    for(let row=0;row < rows;row++){
        for(let col=0;col < cols;col++){
            if (grid[row][col] != 1) continue

            cnt+=1
            let num = 0
            let stack = [[row, col]]

            while(stack.length>0){
                let xy = stack.pop()
                let x = xy[0]
                let y = xy[1]
                grid = twoDimenArrSetVal(x,y,grid,2)

                for(let dir=0;dir<4;dir++){

                    let nx = x + dx[dir]
                    let ny = y + dy[dir]

                    if (nx < 0 || nx >= rows || ny < 0 || ny >= cols){ 
                        num+=1
                        continue
                    } 
                    let checker = twoDimenArrGetVal(nx, ny, grid)
                    if (checker==0) {
                        num+=1
                    } 
                    if (checker != 1) continue
                    stack.push([nx, ny])
                }

            }
            ans[cnt]=num
        }
    }

    console.log("ans", ans)

    return cnt
}

function twoDimenArrGetVal(x,y,arr){

    const oneDimArr = arr[x]
    const val = oneDimArr[y]
    return val

}

function twoDimenArrSetVal(x,y,arr,val){

    const oneDimArr = arr[x]
    oneDimArr[y] = val
    return arr

}

console.log(island_dfs_stack(grid=[
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,1,0,0,0],
    [0,0,0,0,0]
]))