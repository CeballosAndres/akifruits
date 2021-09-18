// $(document).ready(function() {
//     $('form').on('submit', function(event) {
//         $.ajax({
//             data: {
//                 current_node : $('#current-node').val(),
//             },
//             type : 'POST',
//             url : '/next-node'
//         })
//         .done(function(data) {
//             console.log(data)
//         });
        
//         event.preventDefault();
//     });
// });

function getNextNode(res) {
    $.ajax({
        data: {
            current_node : $('#current-node').val(),
            answer : res
        },
        type : 'POST',
        url : '/next-node'
    })
    .done(function(data) {
        console.log(data);
        if (data.body.nLeft && data.body.nRight){
            $('#text').text(data.body.text);
            $('#current-node').val(data.node);
        } else {
            $('#text').text("es " + data.body.text);
            $('#yes').attr({"onclick": "window.location='/end'", "role": "link"});
            $('#no').attr({"onclick": "window.location='/fail/"+data.node+"'", "role": "link"});
        }
    });
};

function visitPage(){
    window.location='http://www.example.com';
}