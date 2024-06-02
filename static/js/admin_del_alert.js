function qual_del()
{
    txt=confirm('Would you like to delete?')
    window.location.href = "{% url 'del_qual' %}?q_id=" + id;
    if(txt==true)
    {
        return true; 
        
    }
    else
    {
        return false;
    }
   
}

function des_del()
{
    txt=confirm('Would you like to delete?')
    window.location.href = "{% url 'del_des' %}?d_id=" + id;
    if(txt==true)
    {
        return true; 
        
    }
    else
    {
        return false;
    }
   
}

function cls_del()
{
    txt=confirm('Would you like to delete?')
    window.location.href = "{% url 'dlt_cls' %}?cl_id=" + id;
    if(txt==true)
    {
        return true; 
        
    }
    else
    {
        return false;
    }
   
}

function div_del()
{
    txt=confirm('Would you like to delete?')
    window.location.href = "{% url 'dlt_div' %}?div_id=" + id;
    if(txt==true)
    {
        return true; 
        
    }
    else
    {
        return false;
    }
   
}
