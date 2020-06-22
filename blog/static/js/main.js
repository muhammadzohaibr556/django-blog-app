setTimeout(function() {
    $('#message').fadeOut('slow');
  }, 300);


function del(title,id)
{
    document.getElementById("tit").innerHTML = title;
    document.getElementById("input_id").value = id;
}
/*function edity(id,title,desc)
{
    alert("{% url 'update_post'"+id+"%}");
    document.all("title").value = title;
    document.all("desc").value = desc;
    form.all("edit_post_form").action = "{% url 'update_post'"+id+"%}"
}
function info(username, email, country)
{
    document.getElementById("edit_user").value = username;
    document.getElementById("edit_email").value = email;
    document.getElementById("edit_country").value = country;
    alert(username + email + country)
}*/