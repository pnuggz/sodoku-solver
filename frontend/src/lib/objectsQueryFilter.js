const ObjectsQueryFilter = props => {
  const q = props.query;
  const objects = props.objects;
  const key = props.key || "value";

  if (q === "") {
    return objects;
  }

  const words = q
    .split(/\s+/g)
    .map(s => s.trim())
    .filter(s => !!s);

  const queryResults = objects.reduce((results, obj) => {
    const string = obj[key].toLowerCase();

    const checker = words.reduce((resultsBool, word) => {
      let tester = false;
      if (string.indexOf(word.toLowerCase()) > -1) {
        tester = true;
      }
      return resultsBool && tester;
    }, true);

    if (checker) {
      results.push(obj);
    }
    return results;
  }, []);

  if (queryResults.length === 0) {
    return [
      {
        id: 0,
        [key]: "No item found."
      }
    ];
  }
  return queryResults;
};

export default ObjectsQueryFilter;
