/**
 * This file contains utility methods used on the server.
 * @author Alvin Lin (alvin.lin@stuypulse.com)
 */

function getNormalizedChampionName(champion) {
  return champion.replace('/[^a-zA-Z]', '').toLowerCase();
};

module.exports.getNormalizedChampionName = getNormalizedChampionName;
