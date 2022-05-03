let A = [ -3,-3 ];


function solution (A) {
    let hills = 0;
    let valley = 0;

    let Q = 0;
    for (let P = 0; P < A.length; P++)
    {
        Q = P + 1;
        if(P==0)
        {
            if(0 > A[P])
                valley++;
            else if( 0 < A[P])
                hills ++;
            continue;
        }
        if(Q==A.length-1)
        {
            if(A[Q-1] > 0)
                hills++;
            else if(A[Q-1] < 0)
                valley ++;
            continue;
        }
        if (P > 0 && Q < A.length-1)
        {
            if (A[P - 1] < A[P] && A[Q + 1] < A[Q])
            { hills++; }
            else if (A[P - 1] > A[P] && A[Q + 1] > A[Q])
            { valley++; }
        }

    }
    return hills + valley;

}

console.log(solution(A))