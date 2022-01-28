function ajax(pageNumber) {
  var sortingValiums = document.getElementById("id_sorting");
  var filtersValiums = document.getElementById("id_fields_name");
  var filters = document.getElementById("id_expressions");
  var Valiums = document.getElementById("id_value");
    $.ajax({
        url: '/httpResponse',// Оброшение странице
        type: "get",
        data: {'pageNumber': pageNumber, 'sorting':sortingValiums.value, 'fields_name':filtersValiums.value, 'expressions':filters.value, 'value':Valiums.value},
        dataType: 'json'
          }).done(function(data){
            console.log(data);
         //  let arr = [];
         //  for (let index = 0; index < data.length; index++) {
         //   arr.push(data[index].fields);
         // }
          // console.log(arr)
           let dataTable = data.map(function(data){
             return data.fields;
           })
           console.log(dataTable);
           $('#table tbody').empty();
          for (let index = 0; index < dataTable.length; index++) {
            const element = dataTable[index];
            $('#testTmpl').tmpl(element).appendTo('#table tbody');
          }
        })
      }