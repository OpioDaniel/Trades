function AdvancedTabsManager(my_name, body_,activate_function_link=activate_function_link, is_show_btns=true)
{
 this.my_name=my_name;
 this.elm_body=body_;
 this.activate_function_link_=activate_function_link;

 this.container=null;
 this.titles=null;

 this.tabs={};

//alert(is_show_btns)

 //if(is_show_btns == true)
 //{
   this.create_add_delete_btns();
 //}

 this.init_create_containers();

 this.setTabs();
}

AdvancedTabsManager.prototype.create_add_delete_btns = function()
{
  this.add_btn = document.createElement("button");
  this.add_btn.innerHTML = "Add Tab"
  this.add_btn.addEventListener("click", function(){
      var tab_name_ = prompt("Enter name for new tab:" , '');
      if(tab_name_ == '') {alert("Please enter a tab name"); return;}
      var dic_ = {"obj" : "AdvancedTabs", "atm": atm_.my_name, "fun": "add_tab", "params": {"tab_name": tab_name_}}
      //alert(JSON.stringify(dic_))
      //alert(atm_.activate_function_link_)

             $.post(atm_.activate_function_link_,
                  {
                    dic : JSON.stringify(dic_)
                  },
                  function(dic){
                    //alert(JSON.stringify(dic))
                    var tab_id_ = dic["result"]["tab_id"];
                    atm.tabs[tab_id_] = new Tab(atm, my_name=tab_name_, html="", id=tab_id_);
                    atm.tabs[tab_id_].btn.click();
                  }.bind(atm=atm_));
      }.bind(atm_=this, event))

  this.delete_btn = document.createElement("button");
  this.delete_btn.innerHTML = "Delete Tab"
  this.delete_btn.addEventListener("click", function(){
       var tab_name_ = prompt("Enter name of a tab to delete:" , '')
       if(tab_name_ == '') {alert("Please enter a tab name"); return;}
       var dic_ = {"obj" : "AdvancedTabs", "atm": atm_.my_name, "fun": "delete_tab", "params": {"tab_name": tab_name_}}
       // alert(JSON.stringify(dic_))
              $.post(atm_.activate_function_link_,
              {
                dic : JSON.stringify(dic_)
              },
              function(dic){
                //alert(JSON.stringify(dic))
                var tab_id_ = dic["result"]["tab_id"];
                atm.delete_tab(tab_id_, tab_name_);
             }.bind(atm=atm_))
  }.bind(atm_=this, event))

  this.source_btn = document.createElement("button");
  this.source_btn.innerHTML = "Source"
  this.source_btn.addEventListener("click", function(){

  alert("source")
   editor = PopWin(my_name_="editor", win_name_="editor", win_title_="editor", user_id=1, tab_obj_=atm_.tabs[2])
   alert(9)
   editor.set_win_frame_style("20", "505", "500", "45%", "45%", "white")
   editor.set_acWinStatEventListeners(editor);

  }.bind(atm_=this, event))

  this.elm_body.appendChild(this.add_btn);
  this.elm_body.appendChild(this.delete_btn);
  this.elm_body.appendChild(this.source_btn);
}

AdvancedTabsManager.prototype.init_create_containers = function()
{
   this.titles = document.createElement("div");
   this.titles.setAttribute("id", "tabs_container");
   this.titles.setAttribute("class", "tab");

   this.container = document.createElement("div");
   this.container.setAttribute("id", "tab_contents");
   this.elm_body.appendChild(this.titles);this.elm_body.appendChild(this.container);
}

AdvancedTabsManager.prototype.setTabs = function()
{
  var dic_ = {"obj" : "AdvancedTabs", "atm": this.my_name, "fun": "get_tabs_from_table", "params": {"name": "amos"}}
  //alert(JSON.stringify(dic_))
  $.post(atm_.activate_function_link_,
      {
         dic : JSON.stringify(dic_)
      },
      function(dic){
                //alert(JSON.stringify(dic))

                alert(dic["status"])
          var result = dic["result"]
          for (id_ in result)
          {
            atm_.tabs[id_] = new Tab(this, my_name=result[id_]["tab_name"], html=result[id_]["tab_text"],
            tab_functions=result[id_]["tab_functions"], id=id_);
          }
     }.bind(atm_ = this)
 );
}

AdvancedTabsManager.prototype.delete_tab = function(tab_id_, tab_name_)
{this.tabs[tab_id_].btn.outerHTML="";this.tabs[tab_id_].content.outerHTML="";}


// Tab obj ---
function Tab(parent, my_name, html, tab_functions, id)
{
 eval(tab_functions);
 this.parent = parent;
 this.tab_name = my_name;
 this.html = html;  // "<h1>"+this.tab_name+"</h1>";
 this.tab_id = id;
 this.btn = null;
 this.content = null;
 this.create_title_div();
 this.PopWinObjects = {}
}

Tab.prototype.create_title_div = function()
{
  this.btn = document.createElement("button");
  this.btn.setAttribute("tab_id", this.tab_id);
  this.btn.setAttribute("class", "tablinks");
  this.btn.innerHTML = this.tab_name;
  this.btn.onclick = function(event)
  {
    var elm = event.target;
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
         atm.tabs[tab_id].content.style.display = "block";
         event.currentTarget.className += " active";
    }.bind(atm=this.parent)

    this.btn.click();
    this.btn.className += " active";
    this.parent.titles.appendChild(this.btn)

    this.content = document.createElement("div");
    this.content.setAttribute("tab_id", this.tab_id);
    this.content.setAttribute("class", "tabcontent");
    this.parent.container.appendChild(this.content)
    this.content.innerHTML = this.html;
}











// Win --
function acWin()
{
  // create its div for window

alert(12002)
  // --
  this.set_title_colors("a", "b")
alert(1200211)

}

acWin.prototype.set_title_colors = function(color, b_color)
{

alert(1211)

}


function PopWin(my_name_, win_name_, win_title_, user_id, tab_obj_)
{

alert(111)
  acWin.call()
alert(12)
  this.tab_obj_.PopWinObjects[this.my_name] = this;
alert(12)
}
PopWin.prototype = Object.create(acWin.prototype)