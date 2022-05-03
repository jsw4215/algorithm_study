/**
 * @param {number} n
 * @param {number[][]} reservedSeats
 * @return {number}
 */
 function maxNumberOfFamilies (n, S) {
    const groupReservedSeatsByRow = {};
    const rows = [];

    reservedSeats = S.split(" ")
    console.log("reservedSeats", reservedSeats)
    for (let i = 0; i < reservedSeats.length; i++) {
        
        const row = reservedSeats[i].slice(0,-1);
        const column = reservedSeats[i].slice(-1);
        console.log("reservedSeats", reservedSeats[i])
 
        console.log("row", row)
        console.log("col", column)
        if (!groupReservedSeatsByRow[row]) {
            rows.push(row);
            groupReservedSeatsByRow[row] = [];
        }
        groupReservedSeatsByRow[row].push(column);
    }
    console.log("groupReservedSeatsByRow", groupReservedSeatsByRow, rows)
    let result = 2 * n;
    for (let i = 0; i < rows.length; i++) {
        result -= countOneRow(groupReservedSeatsByRow[rows[i]]);
    }
    return result;
};

const b = [
    2, 3, 4, 5, ];
const c = [
    4, 5, 6, 7, ];
const d = [
    6, 7, 8, 9, ];

function countOneRow (reserve) {
    
    let reserved = reserve.map((item)=>{
        if(item=='A'){
            return 1
        }
        else if(item=='B'){
            return 2
        }
        else if(item=='C'){
            return 3
        }
        else if(item=='D'){
            return 4
        }
        else if(item=='E'){
            return 5
        }
        else if(item=='F'){
            return 6
        }
        else if(item=='G'){
            return 7
        }
        else if(item=='H'){
            return 8
        }
        else if(item=='J'){
            return 9
        }
        else if(item=='K'){
            return 10
        }

    })

    const seats = new Array(11).fill(true);
    reserved.forEach((index) => {
        seats[index] = false;
    });
    console.log("reserved", reserved, seats)

    const left = b.every(index => seats[index]);
    const right = d.every(index => seats[index]);

    console.log("left, right", left, right)

    if (left && right) {
        return 0;
    } else if (left || right) {
        return 1;
    } else {
        return c.every(index => seats[index]) ? 1 : 2;
    }
}

let n = 2;
let resSeats = "1A 2F 1C"
//[1A, 2F, 1C]

console.log("max", maxNumberOfFamilies(n, resSeats))