/**
 * add an aphostrophes to the string or an array
 * @param {string|array} value - the value to that aphostrophes are added
 * @return {string|array} newValue - the same value but with the apostrophes added*/
export default function addApostrophes (value) {
    if (Array.isArray(value) && value.every(item => typeof item === 'string')) {
        let newValues = [];
        for (let i = 0; i < value.length; i++) {
            newValues.push(`'${value[i]}'`);
        }
        return newValues;
    }
    else if (typeof value === "string") {
        let newValue = "";
        return `'${value}'`
    }
}
