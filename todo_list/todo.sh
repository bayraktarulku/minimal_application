# #!/bin/sh

VERSION="1.0.0"
ROOT_DIR=todo
ROOT_FILE=todolist

show_help () {
    cat help
}

add_todo () {
    declare max_count=`tail -1 $ROOT_FILE | cut -d':' -f 1`
    declare max_count=$(($max_count+1))

    if [ $# = 0 ];then
        echo "run 'todo -h' for help"
    fi

    if [ $# = 1 ];then
        echo "$max_count : $1" >> $ROOT_FILE
        echo "New Todo Added!"
        echo "run 'todo -l' for listing all todos."
    fi

    if [ $# -gt 1 ];then
        count=$#
        for param in $@
        do
            var=$var" "$param
        done
        echo "$max_count : $var" >> $ROOT_FILE
        echo "New Todo Added!"
        echo "run 'todo -l' for listing all todos."
    fi
}

delete_todo () {

    list_todos
    echo ''
    read -p '> Todo id : ' id_to_delete
    declare max_count=`tail -1 $ROOT_FILE | cut -d':' -f 1`
    echo $max_count
    if [ $id_to_delete -le $max_count ]
        then
            grep -v "^$id_to_delete " $ROOT_FILE > $ROOT_DIR/tmp && mv $ROOT_DIR/tmp $ROOT_FILE
            echo "Successfully"
        else
            echo "The ID's todo does not exists."
    fi
}

list_todos () {
    echo $ROOT_FILE
    declare total=`wc -l < $ROOT_FILE`
    echo "===================================================================="
    echo "||                            TODO LIST                           ||"
    echo "===================================================================="
    echo "ID : Title                                             Total: "$total
    echo "--------------------------------------------------------------------"
    cat $ROOT_FILE | sort
    echo "===================================================================="
}

reset_todos () {
    cp /dev/null $ROOT_FILE
    echo 'Delete All Todos'
}

initialize () {

    if [ ! -d $ROOT_DIR ];then
        mkdir $ROOT_DIR
    fi

    if [ ! -f $ROOT_FILE ];then
        touch $ROOT_FILE
    fi

}

initialize
case $1 in
    "-a"|"--add"|"add")
        add_todo ${*:2}
        ;;
    "-d"|"--delete"|"delete")
        delete_todo
        ;;
    "-h"|"--help"|"help")
        show_help
        ;;
    "-l"|"--list"|"list")
        list_todos
        ;;
    "-r"|"--reset"|"reset")
        reset_todos
        ;;
    *)
        echo "run 'todo -h' for help"
        ;;
esac
