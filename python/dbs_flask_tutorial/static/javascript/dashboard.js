// Modal. ======================================================================

// Get the modal
var modal = document.getElementsByClassName("modal")[0];
// When the user clicks the link, open the modal
var selectedExpenseId = 0;
function openModal(expenseId) {
    selectedExpenseId = expenseId;
    modal.style.display = "block";
}

// Get the button element that closes the modal
var modalCancel = document.getElementsByClassName("modal-cancel")[0];
// When the user clicks on <span> (x), close the modal
modalCancel.onclick = function() {
    modal.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// When the user clicks the delete button, delete expense from the database.
var modalDelete = document.getElementsByClassName("modal-delete")[0];
modalDelete.onclick = function() {
    var baseUrl = window.location.origin;
    var deleteExpenseUrl = baseUrl + '/deleteExpense/' + selectedExpenseId;
    // Use location.replace to redirect without creating history, else use location.assign.
    location.replace(deleteExpenseUrl);
}

// Table and chart views. ======================================================
function updateView() {  
    var selectView = document.getElementById('selectView');
    var option = selectView.options[selectView.selectedIndex];
    // Loop through all child elements.
    var expensesView = document.getElementById("expenses-view");
    var children = expensesView.children;
    for (var i=0; i<children.length; i++) {
        children[i].style.display = "none";
        if (children[i].id === option.value) {
            children[i].style.display = "block";
            if (option.value === "table") {
                children[i].style.display = "table";
            }
        }
    }
}
updateView();

// Sort by table column. =======================================================

// Convert string date back to time stamp. 
function toTimeStamp(strDate) {
    return Date.parse(strDate)/1000;  
}

var orderBy = "desc";
function sortTable(n) {
    // Toggle orderBy.
    orderBy==="desc" ? orderBy="asc" : orderBy="desc";
    var table = document.getElementById("table");
    var rows = table.rows;
    // Bubble sort.
    for (var i=rows.length-1; i>0; i--) {
        for (var j=1; j<i; j++) {
            var x = rows[j].getElementsByTagName("TD")[n];
            var y = rows[j+1].getElementsByTagName("TD")[n];
            // Budget, sort by float.
            if (n === 1) {
                if (orderBy==="asc" && parseFloat(x.innerHTML.substring(1))>parseFloat(y.innerHTML.substring(1))) {
                    rows[j].parentNode.insertBefore(rows[j+1], rows[j]);
                }
                else if (orderBy==="desc" && parseFloat(x.innerHTML.substring(1))<parseFloat(y.innerHTML.substring(1))) {
                    rows[j].parentNode.insertBefore(rows[j+1], rows[j]);
                }
            }
            // Updated At, sort by time stamp.            
            else if (n === 2) {
                if (orderBy==="asc" && toTimeStamp(x.innerHTML)>toTimeStamp(y.innerHTML)) {
                    rows[j].parentNode.insertBefore(rows[j+1], rows[j]);
                }
                else if (orderBy==="desc" && toTimeStamp(x.innerHTML)<toTimeStamp(y.innerHTML)) {
                    rows[j].parentNode.insertBefore(rows[j+1], rows[j]);
                }
            }
            // The rest sort by string.
            else {
                if (orderBy==="asc" && x.innerHTML.toLowerCase()>y.innerHTML.toLowerCase()) {
                    rows[j].parentNode.insertBefore(rows[j+1], rows[j]);
                }
                else if (orderBy==="desc" && x.innerHTML.toLowerCase()<y.innerHTML.toLowerCase()) {
                    rows[j].parentNode.insertBefore(rows[j+1], rows[j]);
                }
            }
        }
    }
}