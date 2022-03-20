function AdvancedTabs(bdy,add_tab_link, delete_tab_link, get_tabs_from_table_link, tab_div_content_link)
{
this.bdy = bdy;
this.add_tab_link_ = add_tab_link;
this.tab_div_content_link_ = tab_div_content_link;
this.delete_tab_link_ = delete_tab_link;
this.get_tabs_from_table_link_ = get_tabs_from_table_link;
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
      $.post(elm.add_tab_link_,
             {
             'tab_name':tab_name_

             },
             function(dic)
             {
             //alert(dic['status']);alert(dic['tab_id'])
             var tab_id_ = dic['tab_id']
             //alert(tab_id_); alert(tab_name_)
             elm.tabs[tab_id_] = new Tab(elm, tab_id=tab_id_, tab_name=tab_name_);
             }.bind(elm = this));
     }.bind(elm = this))

     this.delete_tab_btn = document.createElement('button')
     this.delete_tab_btn.innerHTML = 'Delete Tabs'
     //alert(this.delete_tab_btn.outerHTML)
     this.delete_tab_btn.addEventListener('click', function()
     {
     var tab_name_ = prompt('Enter New Tab', '')
     if(tab_name_==""){alert("You Must Enter A Tab Name")}
      $.post(elm.delete_tab_link_,
             {
             'tab_name':tab_name_,
             },
             function(dic)
             {
             //alert(dic['status']);alert(dic['tab_id'])
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
 $.post(this.get_tabs_from_table_link_,
       {},
       function(dic)
       {
       for (id in dic)
          {
          //alert(dic[id]["tab_name"])
          //alert(dic[id]["tab_text"])
          elm.tabs[id] = new Tab(elm,tab_id=id, tab_name=dic[id]["tab_name"]);
          }
          elm.tab_container_div.children[0].click();
       }.bind(elm = this)
 )
}

function Tab(parent, tab_id, tab_name)
{
this.parent = parent;
this.tab_id = tab_id;
this.tab_name = tab_name;
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

      var this_elm = this;
      $.post(this.parent.tab_div_content_link_,
             {
             name:this.tab_name
             },
             function(data)
             {
              //alert(data)
              this_elm.tab_div_content.innerHTML = data;
             })
}