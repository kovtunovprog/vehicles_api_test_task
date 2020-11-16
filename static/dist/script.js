console.log('Hello world');


function addElemInGetId() {
    if (this.readyState === 4 && this.status === 201) {
        console.log('hello');
        var myArr = this.responseText;
        $('#get-vehicle-results').append('<p class="success-result">success: ' + this.status + '</p><p class="result-text">' + myArr + '</p>')
    }
    if (this.status !== 201) {
        $('#get-vehicle-results').append('<p class="error-result">error: ' + this.status + '</p><p class="result-text">' + this.responseText + '</p>')
    }
}

function addElemInList() {
    if (this.readyState === 4 && this.status === 200) {
        var myArr = this.responseText;
        $('#list-vehicle-results').append('<p class="success-result">success: ' + this.status + '</p><p class="result-text">' + myArr + '</p>')
    }
    if (this.status !== 200) {
        $('#list-vehicle-results').append('<p class="error-result">error: ' + this.status + '</p><p class="result-text">' + this.responseText + '</p>')
    }
}

function addElementInFiltered() {
    if (this.readyState === 4 && this.status === 200) {
        var myArr = this.responseText;
        $('#filtered-vehicle-result').append('<p class="success-result">success: ' + this.status + '</p><p class="result-text">' + myArr + '</p>')

    }
    if (this.status !== 200) {
        $('#filtered-vehicle-result').append('<p class=\'error-result\'>error: ' + this.status + '</p><p class="result-text">' + this.responseText + '</p>')
    }
}

function addElemInAdd() {
    if (this.readyState === 4 && this.status === 201) {
        var myArr = this.responseText;
        $('#add-vehicle-results').append('<p class="success-result">success: ' + this.status + '</p><p class="result-text">' + myArr + '</p>');
    }
    if (this.status !== 201) {
        $('#add-vehicle-results').append('<p class="error-result">error: ' + this.status + '</p><p class="result-text">' + this.responseText + '</p>')
    }
}

function addElemInEdit() {
    if (this.readyState === 4 && this.status === 202) {
        var myArr = this.responseText;
        $('#edit-vehicle-results').append('<p class="success-result">success: ' + this.status + '</p>')
    }
    if (this.status !== 202) {
        $('#edit-vehicle-results').append('<p class="error-result">error: ' + this.status + '</p><p class="result-text">' + this.responseText + '</p>')
    }
}

function addElemInDel() {
    if (this.readyState === 4 && this.status === 204) {
        var myArr = this.responseText;
        console.log(myArr);
        $('#del-vehicle-results').append('p class="success-result">success: ' + this.status + '</p>')
    }
    if (this.status !== 204) {
        $('#del-vehicle-results').append('<p class="error-result">error: ' + this.status + '</p><p class="result-text">' + this.responseText + '</p>')
    }
}

function getData(method, url, ready_func, body=null) {
    var xhr = new XMLHttpRequest();
    xhr.open(method, url, true);
    // xhr.responseType = 'json';
    if (body === null) {
        xhr.send()
    }
    else {
        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        console.log(body);
        xhr.send(JSON.stringify(body))
    }
    xhr.onreadystatechange = ready_func;
    return xhr
}

function getVehicle() {
    var id = $('#get_id').val();
    var url = 'api/1.0/vehicles/' + id;
    getData('GET', url, addElemInGetId)
}

function getList() {
    var url = 'api/1.0/vehicles';
    getData('GET', url, addElemInList)
}

function filtered() {
    var vendor = $('#vendor-filtered').val();
    var model = $('#model-filtered').val();
    var year = $('#year-filtered').val();
    var color = $('#color-filtered').val();
    var vin = $('#VIN-filtered').val();

    $('#vendor-filtered').val("");
    $('#model-filtered').val("");
    $('#year-filtered').val("");
    $('#color-filtered').val("");
    $('#VIN-filtered').val("");

    var params = "vendor=" + vendor + "&model=" + model + "&year=" + year + "&color=" + color + "&vin=" + vin;
    var url = 'api/1.0/vehicles?' + params;
    console.log(url);
    getData('GET', url, addElementInFiltered)
}

function addVeh() {
    var vendor = $('#vendor-add').val();
    var model = $('#model-add').val();
    var year = $('#year-add').val();
    var color = $('#color-add').val();
    var vin = $('#VIN-add').val();

    var body = {
        'vendor': vendor,
        'model': model,
        'year': year,
        'color': color,
        'vin': vin
    };
    var url = 'api/1.0/vehicles';
    getData('POST', url, addElemInAdd, body)
}

function editVeh() {
    var id = $('#edit-id').val();
    var vendor = $('#vendor-edit').val();
    var model = $('#model-edit').val();
    var year = $('#year-edit').val();
    var color = $('#color-edit').val();
    var vin = $('#VIN-edit').val();

    $('#edit-id').val("");
    $('#vendor-edit').val("");
    $('#model-edit').val("");
    $('#year-edit').val("");
    $('#color-edit').val("");
    $('#VIN-edit').val("");

    var body = {'vendor': vendor, 'model': model, 'year': year, 'color': color, 'vin': vin};
    var url = 'api/1.0/vehicles/' + id;
    getData('PUT', url, addElemInEdit, body)
}

function delVeh(){
    var id = $('#del_id').val();
    var url = 'api/1.0/vehicles/' + id;
    var body = {'id': id};
    getData('DELETE', url, addElemInDel, body)
}


$('#button-get-vehicle').click(getVehicle);
$('#button-get-list').click(getList);
$('#button-filtered').click(filtered);
$('#button-add').click(addVeh);
$('#button-edit').click(editVeh);
$('#button-del').click(delVeh);





