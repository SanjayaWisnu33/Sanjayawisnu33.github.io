---
title : "Scraping"
permalink : /scrap/
---

<h1>SCRAPING</h2>

<script src="https://code.jquery.com/jquery-3.3.1"></script>
<script>
    $(function() {
        $.get('D:\CODE\PROYEK\Py\headline.txt', function(obj) {
            var judul = obj.split("\n");
            str = "<table border= '1'><tr><td>No</td><td>Judul Head</td></tr>";
            $.each(judul, function(n,judul) {
                str+="<tr><td>"+(n+1)+"</td>";
                str+="<td>"+judul+"</td>";
            });
        });
        alert(str)
        $('#headline').html(str);
    });
</script>
  
