function createDataTransfer() {
    return {
        data: {},
        setData: function (key, value) {
            this.data[key] = value;
        },
        getData: function (key) {
            return this.data[key]
        }
    };
}

function createEvent(eventType, dataTransfer) {
    var event = document.createEvent("CustomEvent");
    event.initCustomEvent(eventType, true, true, null);
    event.dataTransfer = dataTransfer;
    return event;
}

function dispatchOrFireEvent(element, event) {
    if (element.dispatchEvent) {
        element.dispatchEvent(event);
    } else if (element.fireEvent) {
        element.fireEvent("on" + event.type, event);
    }
}

function executeHTML5DragAndDrop(element, destination) {
    var dataTransfer = createDataTransfer()
    var dragStartEvent = createEvent('dragstart', dataTransfer);
    var dropEvent = createEvent('drop', dataTransfer);
    var dragEndEvent = createEvent('dragend', dataTransfer);
    dispatchOrFireEvent(element, dragStartEvent);
    dispatchOrFireEvent(destination, dropEvent);
    dispatchOrFireEvent(element, dragEndEvent);
}

var source = arguments[0];
var destination = arguments[1];
executeHTML5DragAndDrop(source, destination);
