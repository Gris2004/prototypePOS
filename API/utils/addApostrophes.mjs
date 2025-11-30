/**
 * add an aphostrophes to the string or an array
 * @param {string|array} value - the value to that aphostrophes are added
 * @return {string|array} newValue - the same value but with the apostrophes added*/
export default function addApostrophes (value) {
    try {
        if(Array.isArray(value)) {
            let newValue = [];
            for(let i = 0; i < value.length; i++){
                if(typeof value[i] === "string") newValue.push(`'${value[i]}'`);
                else newValue.push(value[i]);
            }
            return newValue
        } 
        else if (typeof value === "string") {
            let newValue = "";
            return `'${value}'`
        }
    } catch (err) {
        return `Error message: ${err}`;
    }
}
