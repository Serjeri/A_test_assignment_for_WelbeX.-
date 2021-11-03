function ajax(pageNumber) {
    $.ajax({
        url: '/httpResponse',// Оброшение странице
        type: "get",
        data: {'pageNumber': pageNumber},
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
           const rows = $('#table tbody tr');
          for (let index = 0; index < dataTable.length; index++) {
            const element = dataTable[index];
            const row = rows.get(index);
            $($(row).find('td').get(0)).text(element.data)
            $($(row).find('td').get(1)).text(element.title)
            $($(row).find('td').get(2)).text(element.quantity)
            $($(row).find('td').get(3)).text(element.distance)
          }
        })
      }