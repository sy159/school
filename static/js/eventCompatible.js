/**
 * Created by gmx on 2018/4/18.
 */
var eventCompatible={
    e:function (e) {
        return e || event
    },
    getDocProp: function (prop_name) {
        return document.documentElement[prop_name] || document.body[prop_name];
    },
    addEvent: function (obj,event,func){
        if(obj.addEventListener){
            obj.addEventListener(event,func,false)
        }
        else if(obj.attachEvent){
            obj.attachEvent('on'+event,func)
        }
        else{
            obj['on'+event]=func;
        }
    },
    removeEvent: function (obj,event,func){
        if(obj.removeEventListener){
            obj.removeEventListener(event,func,false)
        }
        else if(obj.detachEvent){
            obj.attachEvent('on'+event,func)
        }
        else{
            obj['on'+event]=null;
        }
    },
    preventDefault:function(e){
        if(e.preventDefault){
            e.preventDefault();
        }
        else{
            e.returnValue=false;
        }
    },
    stopPropagation:function(e){
        if(e.stopPropagation){
            e.stopPropagation();
        }else{
            e.cancelBubble=true;
        }
    },
    agentEvent: function (ancestor,event,aEl,func){
        this.addEvent(ancestor,event, function (ev) {
            var e=ev||window.event;
            var target= e.target || e.srcElement;
            while(target!= e.currentTarget){//toUpperCase()×ª´óÐ´
                if(target.nodeName==aEl[0].toUpperCase() && target.classList.contains(aEl[1])){
                    func.call(target);
                    break;
                }
                target=target.parentNode;
            }
        });
    }
}