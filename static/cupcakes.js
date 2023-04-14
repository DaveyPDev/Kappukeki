const BASE_URL = "http://127.0.0.1:5000/api";

/* generate cupcake html */
function createCupcakeHTML(cupcake) {
    return `<div data-cupcake-id=${cupcake.id}>
    <li>
    ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
    <button class='delete-button'>X</button>
    </li>
    <img class='cupcake-img'
        src='${cupcake.image}'
        alt='(No image)' ></img>
    </div>`;
}

/* cupcakes page */
async function showInitalCupcake() {
    const response = await axios.get(`${BASE_URL}/cupcakes`)

    for (let cupcakeData of response.data.cupcakes) {
        let newCupcake = $(createCupcakeHTML(cupcakeData));
        $('#cupcakes-list').append(newCupcake)
    }
}

/* handle cupcake form */

$('#new-cupcake-form').on('submit', async function (e) {
    e.preventDefault();

    let flavor = $('#flavor-form').val();
    let rating = $('#rating-form').val();
    let size = $('#size-form').val();
    let image = $('#image-form').val();

    console.log(`Flavor: ${flavor}, Rating: ${rating}, Size: ${size}, Image: ${image}`);

    const newCupcakeResp = await axios.post(`${BASE_URL}/cupcakes`, {
        flavor,
        rating,
        size,
        image
    }, { withCredentials: true});

    let newCupcake = $(createCupcakeHTML(newCupcakeResp.data.cupcake));
    $('#cupcakes-list').append(newCupcake);
    $('#new-cupcake-form').trigger('reset');
});

$('#cupcakes-list').on('click','.delete-button', async function (e) {
    e.preventDefault();

    let $cupcake = $(e.target).closest('div');
    let cupcakeId = $cupcake.attr('data-cupcake-id');

    await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
    $cupcake.remove();
})

$(showInitalCupcake);


