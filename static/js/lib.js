$(document).ready(function () {
    localStorage.removeItem('nodes');
    $('.without-nodes').hide();
});

function getNextNode(res) {
    $.ajax({
            data: {
                current_node: $('#current-node').val(),
                answer: res
            },
            type: 'POST',
            url: '/next-node'
        })
        .done(function (data) {
            // Controla si se trata de hoja o de un padre
            if (data.error) {
                $('#yes').attr({
                    "onclick": "window.location='/end'",
                    "role": "link"
                });
                $('#no').attr({
                    "onclick": "window.location='/fail/" + $('#current-node').val() + "'",
                    "role": "link"
                });
            } else {
                if (data.body.nLeft && data.body.nRight) {
                    // En caso de que sea padre
                    $('#text').text(data.body.text);

                    $('#current-node').val(data.node);
                    $('#right-node').val(data.body.nRight);
                    $('#left-node').val(data.body.nLeft);
                    $('#yes').attr({
                        "onclick": "getNextNode('yes')"
                    });
                    $('#no').attr({
                        "onclick": "getNextNode('no')"
                    });
                    $('#image').hide();
                    $('#description').hide();
                    $('#scientific-name').hide();
                    $('#nose').show();
                } else {
                    // En caso de que sea hoja
                    if (data.body.description) {
                        $('#description').text(data.body.description);
                        $('#description').show();
                    }
                    if (data.body['scientific-name']) {
                        $('#scientific-name').text(data.body['scientific-name']);
                        $('#scientific-name').show();
                        $('#scientific-name-p').show();
                    }

                    if (data.body.img){
                        $('#image').attr("src", data.body.img);
                        $('#image').show(); 
                    }

                    $('#text').text("es " + data.body.text);
                    $('#nose').hide();
                    $('#yes').attr({
                        "onclick": "window.location='/end'",
                        "role": "link"
                    });
                    $('#no').attr({
                        "onclick": "window.location='/fail/" + data.node + "'",
                        "role": "link"
                    });
                    if (localStorage.getItem('nodes')) {
                        $('#current-node').val(pushLocalNode());
                        $('#no').attr({
                            "onclick": "getNextNode('no')"
                        });
                    }
                }
            }
            // Manejo de camino alternativo para árbol
            let number = $('#question-number').text();
            $('#question-number').text(parseInt(number) + 1);
        });
};

function pushLocalNode() {
    let localData = localStorage.getItem('nodes');
    let nodes = JSON.parse(localData);
    let node = nodes.shift();
    if (nodes.length == 0) {
        localStorage.removeItem('nodes');
    } else {
        localStorage.setItem('nodes', JSON.stringify(nodes));
    }
    return node;
}

function saveNode() {
    let node = $('#right-node').val();
    if (localStorage.getItem('nodes')) {
        // En caso de que existan nodos guardados
        let nodes = localStorage.getItem('nodes');
        let array = JSON.parse(nodes);
        array.push(node)
        localStorage.setItem('nodes', JSON.stringify(array))
    } else {
        // En caso de que NO existan nodos
        let nodes = [node];
        localStorage.setItem('nodes', JSON.stringify(nodes));
    }
    getNextNode("yes");
}