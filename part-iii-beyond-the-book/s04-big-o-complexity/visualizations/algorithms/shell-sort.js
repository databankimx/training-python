/* Shell Sort - step generator for the shared visualization player.
   A generalized Insertion Sort comparing elements a shrinking "gap" apart. The gaps follow the
   Python lesson's shell_sort: 2^k - 1 for k from ceil(log2 n) down to 1 (15, 7, 3, 1 for 16
   items). Watch how far-apart elements jump into place in large strides early on, rather than
   one small shift at a time the way plain Insertion Sort does. */
window.generateSteps = function () {
  const SIZE = 16;

  const array = Array.from({ length: SIZE }, (_, i) => i);
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1)); // NOSONAR
    [array[i], array[j]] = [array[j], array[i]];
  }

  const working = array.slice();
  const steps = [];

  const n = working.length;
  let k = Math.ceil(Math.log2(n));
  let interval = Math.pow(2, k) - 1;

  while (interval > 0) {
    for (let i = interval; i < n; i++) {
      const temp = working[i];
      let j = i;

      while (j >= interval) {
        steps.push({ type: 'compare', indices: [j - interval, j] });
        if (working[j - interval] <= temp) break;
        working[j] = working[j - interval];
        steps.push({ type: 'overwrite', index: j, value: working[j] });
        j -= interval;
      }

      working[j] = temp;
      steps.push({ type: 'overwrite', index: j, value: temp });
    }

    k--;
    interval = Math.pow(2, k) - 1;
  }

  steps.push({ type: 'sorted', indices: Array.from({ length: n }, (_, i) => i) });

  return {
    title: 'Shell Sort - O(n²) worst case, faster in practice',
    description:
      'A generalized Insertion Sort: compares elements a shrinking gap apart (gaps of 2^k - 1, as in the lesson code) before a final adjacent-elements pass - out-of-order elements can jump into place in large strides instead of one small shift at a time.',
    array,
    steps
  };
};
