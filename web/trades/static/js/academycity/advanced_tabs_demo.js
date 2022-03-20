function AdvancedTabs(my_name,bdy, activate_function_link)
{
this.my_name = my_name;
this.bdy = bdy;
this.activate_function_link_ = activate_function_link;
this.create_btn();
this.create_containers_div();
this.tabs = {};
this.get_tabs_from_table();
}

AdvancedTabs.prototype.create_btn = function()
{
     this.add_tab_btn = document.createElement('button')
     this.add_tab_btn.innerHTML = 'Add Tabs'
     //alert(this.add_tab_btn.outerHTML)
     this.add_tab_btn.addEventListener('click', function()
     {
     var tab_name_ = prompt('Enter New Tab', '')
     if(tab_name_==""){alert("You Must Enter A Tab Name")}
     var a_f_l_dic = {'obj':'AdvancedTab', 'atm':this.my_name, 'fun':'add_tab', "params":{'tab_name':tab_name_} }
      $.post(elm.activate_function_link_,
             {
             dic: JSON.stringify(a_f_l_dic)

             },
             function(dic)
             {
              alert(dic['status']);alert(JSON.stringify(dic))
             var tab_id_ = dic['tab_id']
             //alert(tab_id_); alert(tab_name_)
             elm.tabs[tab_id_] = new Tab(elm, tab_id=tab_id_, tab_name=tab_name_, html="");
             }.bind(elm = this));
     }.bind(elm = this))

     this.delete_tab_btn = document.createElement('button')
     this.delete_tab_btn.innerHTML = 'Delete Tabs'
     //alert(this.delete_tab_btn.outerHTML)
     this.delete_tab_btn.addEventListener('click', function()
     {
     var tab_name_ = prompt('Enter New Tab', '')
     if(tab_name_==""){alert("You Must Enter A Tab Name")}
     var a_f_l_dic = {'obj':'AdvancedTab', 'atm':elm.my_name, 'fun':'add_tab', "params":{'tab_name':tab_name_} }
      $.post(elm.activate_function_link_,
             {
             dic: JSON.stringify(a_f_l_dic)
             },
             function(dic)
             {
             alert(dic['status']);alert(dic['tab_id'])
             var tab_id_ = dic['tab_id']
             //alert(tab_id_); alert(tab_name_)
             elm.delete_tab_from_container(tab_id_, tab_name_)
             });

     }.bind(elm = this))

     this.bdy.appendChild(this.add_tab_btn); this.bdy.appendChild(this.delete_tab_btn)
}


AdvancedTabs.prototype.create_containers_div = function()
{
this.tab_container_div = document.createElement('div')
this.tab_container_div.setAttribute('id','tab_container')
this.tab_container_div.setAttribute('class','tab')

this.tab_contents_div = document.createElement('div')
this.tab_contents_div.setAttribute('id','tab_contents')

this.bdy.appendChild(this.tab_container_div); this.bdy.appendChild(this.tab_contents_div)
}


AdvancedTabs.prototype.delete_tab_from_container = function (tab_id_, tab_name_)
{
  this.tabs[tab_id_].btn.outerHTML="";this.tabs[tab_id_].tab_div_content.outerHTML="";
  this.tab_container_div.children[0].click();
}


AdvancedTabs.prototype.get_tabs_from_table = function()
{
var a_f_l_dic = {'obj':'AdvancedTab', 'atm':this.my_name, 'fun':'get_tabs_from_table', "params":{} }
 $.post(this.activate_function_link_,
       {
       dic: JSON.stringify(a_f_l_dic)
       },
       function(dic)
       {
        //alert(JSON.stringify(dic["result"]))
        var result = dic["result"]
       for (id in result)
          {
          //alert(dic[id]["tab_text"])
          elm.tabs[id] = new Tab(elm,tab_id=id, tab_name=result[id]["tab_name"], html=result[id]["tab_text"],
                                 tab_text_function=result[id]["tab_text_function"]);
          }
          elm.tab_container_div.children[0].click();
       }.bind(elm = this)
 )
}

function Tab(parent, tab_id, tab_name, html, tab_text_function)
{
eval(tab_text_function)
//this.tab_text_function =tab_text_function;
this.parent = parent;
this.tab_id = tab_id;
this.tab_name = tab_name;
this.html = html;
this.make_tab_btn_tab_content_div();
}

Tab.prototype.make_tab_btn_tab_content_div = function()
{
      this.btn = document.createElement("button");
      this.btn.setAttribute("tab_id", this.tab_id);
      this.btn.setAttribute("class", "tablinks");
      this.btn.setAttribute("city_name", tab_name);
      this.btn.innerHTML = this.tab_name
      this.btn.addEventListener('click', function()
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
         atm.tabs[tab_id].tab_div_content.style.display = "block";
         event.currentTarget.className += " active";
      }.bind(atm=this.parent)
      )
      this.btn.className += " active";
      this.btn.click();

      this.parent.tab_container_div.appendChild(this.btn)

      this.tab_div_content = document.createElement("div");
      this.tab_div_content.setAttribute("tab_id", this.tab_id);
      this.tab_div_content.setAttribute("class", "tabcontent");
      this.parent.tab_contents_div.appendChild(this.tab_div_content)
      this.tab_div_content.innerHTML = this.html;
      //alert(this.html)

}