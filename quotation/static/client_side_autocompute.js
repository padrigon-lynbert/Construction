const margin = document.getElementById('margin');
const overhead = document.getElementById('overhead');
const tax = document.getElementById('tax');
const subtotal = document.getElementById('subtotal');
const subtotal_details = document.getElementById('subtotal_details');

// calculate costs and subtotal whenever quantity, cost, margin, or tax changes (fire)
function calculateAll() {
    const rows = document.querySelectorAll(".individual_quotation_table table tr");
    let subtotal_value = 0;

    rows.forEach(row => {
        const qtyInput = row.querySelector(".qty");
        const costInput = row.querySelector(".cost");
        const autocostTd = row.querySelector(".autocost");
        if (!qtyInput || !costInput || !autocostTd) return;

        const quantity = parseFloat(qtyInput.value) || 0;
        const unitCost = parseFloat(costInput.value) || 0;
        const totalCost = quantity * unitCost;

        autocostTd.textContent = `₱${totalCost}`;
        subtotal_value += totalCost;
    });

    // apply margin and tax (percentages should compound)
    const overhead_value = parseFloat(overhead.value) || 0;
    const margin_value = parseFloat(margin.value) || 0;
    const tax_value = parseFloat(tax.value) || 0;

    subtotal_value_no_index = subtotal_value;
    subtotal_value_with_overhead = subtotal_value + (overhead_value / 100*subtotal_value);
    vales_with_margin = subtotal_value_with_overhead + (margin_value / 100*subtotal_value_with_overhead);
    vales_with_tax = vales_with_margin + (tax_value / 100*vales_with_margin);

    subtotal_value = vales_with_tax;

    subtotal.textContent = `₱${subtotal_value.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
    subtotal_details.textContent = 
        `₱${subtotal_value_no_index} + ₱${subtotal_value_with_overhead - subtotal_value_no_index}\n` +
        `₱${subtotal_value_with_overhead} + ₱${vales_with_margin - subtotal_value_with_overhead}\n` +
        `₱${vales_with_margin} + ₱${vales_with_tax - vales_with_margin}\n`; 
}

// attach input events
document.querySelectorAll(".qty, .cost").forEach(input => {
    input.addEventListener("input", calculateAll);
});
overhead.addEventListener("input", calculateAll);
margin.addEventListener("input", calculateAll);
tax.addEventListener("input", calculateAll);

calculateAll();