// worker.js
// To run heavy network computations in parallel

// Listen for messages from the main thread
self.onmessage = function(e) {
    const { nodes, links, uniqueLinks, jsonPapers } = e.data;
    
    const numNodes = nodes.length;
	const numLinks = links.length;
    const numUniqueLinks = uniqueLinks.length;
	const numPapers = jsonPapers.length;
    const clusteringCoefficient = calculateClusteringCoefficient(nodes, uniqueLinks);
	//const assortativity = calculateAssortativity(nodes, uniqueLinks);

    // Send the results back to the main thread
	console.log('hello');
    self.postMessage({ numNodes, numLinks, numUniqueLinks, numPapers, clusteringCoefficient });
};


// Function to calculate the clustering coefficient
function calculateClusteringCoefficient(nodes, links) {
	let clusteringSum = 0;

	nodes.forEach(node => {
		const neighbors = links.filter(link => link.source.id === node.id || link.target.id === node.id)
			.map(link => link.source.id === node.id ? link.target : link.source);
		const numNeighbors = neighbors.length;
		if (numNeighbors < 2) return;

		let linksBetweenNeighbors = 0;
		neighbors.forEach((neighbor1, i) => {
			neighbors.slice(i + 1).forEach(neighbor2 => {
				if (links.some(link => (link.source.id === neighbor1.id && link.target.id === neighbor2.id) || (link.source.id === neighbor2.id && link.target.id === neighbor1.id))) {
					linksBetweenNeighbors++;
				}
			});
		});

		clusteringSum += (2 * linksBetweenNeighbors) / (numNeighbors * (numNeighbors - 1));
	});

	return clusteringSum / nodes.length;
}