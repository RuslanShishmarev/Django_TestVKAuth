var all_links = document.getElementById("nav").getElementsByTagName("a");
len=all_links.length,
full_path = location.href.split('#')[0];

for (i=0; i<len; i++){
    if(all_links[i].href.split("#")[0] == full_path) {
        if (all_links[i].id != "out"){
            all_links[i].style.color = "#F9922B";
            all_links[i].style.borderBottom = "4px solid #F9922B";
        }
        else{
             all_links[i].style.background = "#F9922B"
             all_links[i].style.color = "#FFFFFF";
        }
    }
}