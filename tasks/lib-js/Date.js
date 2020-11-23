


const local = 'de-De';
const options =  {year:"numeric",month:"2-digit", day:"2-digit"};

function format( dateInstance ){
    return dateInstance.toLocaleDateString( local, options);
}

exports.format = format
