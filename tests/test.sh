if [ "$1" == "" ]; then
    echo "usage: $0 <test dir...>"
    exit 1
fi

function check() {
    target=$1
    shift 1
    cat ../att/input.txt | "$@" > output.$target.txt
    diff ../att/output.txt <(cat output.$target.txt | sed 's|  0\.0| 0.0|g;s|E[+]00*||g;s|\.00* | |g;s|\.00*$||')
}

function check_cms() {
    dir=$1
    echo "C..."
    gcc $dir.c -o ${dir}_c
    check c ./${dir}_c
    echo "CPP..."
    g++ --std=c++11 $dir.cpp -o ${dir}_cpp
    check cpp ./${dir}_cpp
    echo "JAVA..."
    javac $dir.java
    check java java $dir
    echo "PAS..."
    fpc -v0 $dir.pas -o${dir}_pas | tail -n +3
    rm $dir.o
    check pas ./${dir}_pas
    echo "PY..."
    check py python3 $dir.py
}

function check_terry() {
    echo "CS..."
    csc $dir.cs | tail -n +4
    check cs mono ${dir}.exe
}

for t in "$@"; do
    dir=${t%/}
    cd $dir
    echo
    echo ">> TEST: $dir <<"
    echo
    make-templates --limits limits.py -t
    echo "Terry output generated."
    cd statement
    check_cms $dir
    check_terry $dir
    cd ..
    echo
    make-templates --limits limits.py -c
    echo "CMS output generated."
    cd att
    check_cms $dir
    cd ../..
done
