function AdvancedTabs(my_name, body_=null, is_show_btns=false, add_link, delete_link, get_tabs_from_table_link,
  update_text_tab)
{
 this.my_name = my_name;
 this.elm_body=body_;
 this.add_link_ = add_link;
 this.delete_link_ = delete_link;
 this.get_tabs_from_table_link = get_tabs_from_table_link;
 this.update_text_tab = update_text_tab;
 if(is_show_btns==true){this.init_create_btns(btn_name1="Add Tab", btn_name2="Delete Tab")}
 this.init_create_containers();
 this.get_tabs_from_table();
}
AdvancedTabs.prototype.init_create_containers = function()
{
   this.titles = document.createElement("div");
   this.titles.setAttribute("id", "tabs_container");
   this.titles.setAttribute("class", "tab");
   this.container = document.createElement("div");
   this.container.setAttribute("id", "tab_contents");
   this.elm_body.appendChild(this.titles);this.elm_body.appendChild(this.container);
}
AdvancedTabs.prototype.init_create_btns = function(btn_name)
{
      var add_btn = document.createElement("button");
      add_btn.setAttribute("id", "add_button");
      add_btn.innerHTML = btn_name1
      add_btn.addEventListener("click", function(){
      var tab_name_ = prompt("Enter name for new tab:" , '')
      if(tab_name_ == '') {alert("Please enter a tab name"); return;}
             $.post(elm.add_link_,
                  {
                    tab_name: tab_name_,
                  },
                  function(dic){
                    var tab_id_ = dic["tab_id"];
                    elm.makebtndivtxt(tab_name_, tab_id_, '');
                  }.bind(elm = this)
                  );
      }.bind(elm = this, event))
      var delete_btn = document.createElement("button");
      delete_btn.setAttribute("id", "delete_button");
      delete_btn.innerHTML = btn_name2
      delete_btn.addEventListener("click", function(){

         var tab_name_ = prompt("Enter name of a tab to delete:" , '')
         if(tab_name_ == '') {alert("Please enter a tab name"); return;}
         $.post(elm.delete_link_,
              {
                tab_name: tab_name_,
              },
              function(dic){
                var tab_id_ = dic["tab_id"];
                elm.delete_tab_from_container(tab_id_, tab_name_);
             }
         );
      }.bind(elm = this, event))
      this.elm_body.appendChild(add_btn);this.elm_body.appendChild(delete_btn);
}

AdvancedTabs.prototype.delete_tab_from_container = function (tab_id_, tab_name_)
{
  document.getElementById("tab_title_"+tab_id_).outerHTML = ""
  document.getElementById("tab_div_"+tab_id_).outerHTML = "";
  this.titles.children[0].click();
}

AdvancedTabs.prototype.makebtndivtxt = function(tab_name, tab_id, tab_txt)
{
      var btn = document.createElement("button");
      btn.setAttribute("id", "tab_title_"+tab_id);
      btn.setAttribute("tab_id", tab_id);
      btn.setAttribute("class", "tablinks");
      btn.setAttribute("city_name", tab_name);
      btn.innerHTML = tab_name
      btn.onclick = function open_city(event)
      {
        var elm = event.target
        var tab_id = elm.getAttribute("tab_id")

            var tabcontent = document.getElementsByClassName("tabcontent");
            for(i=0; i<tabcontent.length; i++){
            //alert(tabcontent[i].outerHTML)
            tabcontent[i].style.display = 'none';
            }
            var tablinks = document.getElementsByClassName("tablinks");
            for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
            }
         document.getElementById("tab_div_"+tab_id).style.display = "block";
         event.currentTarget.className += " active";
      }
      this.titles.appendChild(btn)
      var div = document.createElement("div");
      div.setAttribute("id", "tab_div_"+tab_id);
      div.setAttribute("tab_id", tab_id);
      div.setAttribute("class", "tabcontent");
      var txt_ = document.createElement("textarea");
      txt_.setAttribute("id", "tab_txt_"+tab_id);
      txt_.setAttribute("tab_id", tab_id);
      txt_.setAttribute("rows", 10);
      txt_.setAttribute("cols", 30);
      txt_.onchange = function onchange_txt(event){
        var e = event.target;
        var tab_id_ = e.getAttribute("tab_id");
        $.post(elm.update_text_tab,
          {tab_id: tab_id_, value: e.value,},
          function(dic){ }
        );
      }.bind(elm = this)
      div.appendChild(txt_)
      txt_.innerHTML = tab_txt
      this.container.appendChild(div)
      btn.click()
}

AdvancedTabs.prototype.get_tabs_from_table = function()
{
 $.post(this.get_tabs_from_table_link,
      {},
      function(dic){
          for (id in dic)
          {
          //alert(dic[id]["tab_name"])
          //alert(dic[id]["tab_text"])
          //alert(at.add_link_)
          elm.makebtndivtxt(tab_name=dic[id]["tab_name"], tab_id=id, tab_txt=dic[id]["tab_text"])
          }
          elm.titles.children[0].click();
     }.bind(elm = this)
 );
}

